#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import toBytes

from control.components import components
from control.constants import STATE, ERROR, PIN_TYPE, STYLE, COLOR_FORE
from model.library.input_check import is_valid_adm_code
import view.layout.system.oneline as layout_oneline


class adm():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.PLUGIN
        ret_arg = None

        auto_verify = False
        # Auto ADM operation (read from usim_modifier.xml)
        adm_code = arg_components.config.query_adm_code(
            arg_components.modeler.uicc.iccid)
        if arg_arguments == None and adm_code != None and is_valid_adm_code(adm_code):
            print(res.get_string(
                "auto_adm_verifing") % (arg_components.modeler.uicc.iccid), end='')
            auto_verify = True
        else:
            if arg_arguments == None:
                print(res.get_string("input_adm_code"), end='')
            else:
                print(arg_arguments, end='')

            adm_code = input().strip().upper()

            if len(adm_code) == 0:
                out_msg = layout_oneline.layout(arg_string=res.get_string(
                    "terminated_adm_code"), arg_style=STYLE.BRIGHT, arg_fore=COLOR_FORE.YELLOW)
                print(out_msg)
            elif not is_valid_adm_code(adm_code):
                ret_state = STATE.ADM
                ret_arg = res.get_string("invalid_adm_code")

        if len(adm_code) != 0 and ret_arg == None:
            verify_result, reamings = arg_components.modeler.uicc.verify_pin(
                PIN_TYPE.ADM1, toBytes(adm_code))

            if auto_verify == True:
                if verify_result == ERROR.NONE:
                    print(res.get_string("pass"))
                else:
                    print(res.get_string("fail"))

            # If enabled 'configuration.adm', store the adm code for auto verify
            if verify_result == ERROR.NONE and auto_verify != True:
                if arg_components.config.adm == 1:
                    arg_components.config.update_adm_code(
                        arg_components.modeler.uicc.iccid, adm_code)

            if verify_result != ERROR.NONE:
                if reamings == 0:
                    out_msg = layout_oneline(arg_string=res.get_string(
                        "adm_blocked"), arg_style=STYLE.BRIGHT, arg_fore=COLOR_FORE.RED)
                    print(out_msg)
                else:
                    ret_state = STATE.ADM
                    ret_arg = res.get_string("incorrect_adm_code") % (reamings)

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
