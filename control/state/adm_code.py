#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import PACK
from smartcard.util import toBytes, toASCIIBytes, toHexString

from control.components import components
from control.constants import STATE, ERROR, PIN_TYPE, STYLE, COLOR_FORE
from model.library.input_check import is_valid_adm_code
import view.layout.state.adm_code as layout_adm_code


class adm_code():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.ADM_VERIFY
        ret_arg = None
        adm_code = None
        out_msg = ''

        # if 'arg_arguments' exist, means may the auto verify fail
        # so we can't read the adm code from .xml file
        if arg_arguments == None:
            # Auto ADM operation (read from usim_modifier.xml)
            adm_code = arg_components.config.query_adm_code(
                arg_components.modeler.uicc.iccid)
        if adm_code == None:
            if arg_arguments == None:
                if arg_components.config.admhex == 1:
                    out_msg = res.get_string("input_adm_code_hex")
                else:
                    out_msg = res.get_string("input_adm_code")
            else:
                out_msg = arg_arguments
            print(layout_adm_code.layout(arg_msg=out_msg), end='')
            adm_code = input().strip().upper()

            # convert the 8 digits format to 16 hex digit
            if arg_components.config.admhex == 0:
                adm_code_byte = toASCIIBytes(adm_code)
                adm_code = toHexString(adm_code_byte, format=PACK)

            if len(adm_code) == 0:
                ret_state = STATE.PLUGIN
                print(layout_adm_code.layout(
                    arg_msg=res.get_string("terminated_adm_code")))
            elif not is_valid_adm_code(adm_code):
                ret_state = STATE.ADM_CODE
                if arg_components.config.admhex == 1:
                    ret_arg = res.get_string("invalid_adm_code_hex")
                else:
                    ret_arg = res.get_string("invalid_adm_code")

        if ret_state == STATE.ADM_VERIFY:
            ret_arg = adm_code

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
