#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import toBytes

from control.components import components
from control.constants import STATE, ERROR, PIN_TYPE, STYLE, COLOR_FORE
from model.library.input_check import is_valid_adm_code
import view.layout.state.adm as layout_adm


class adm():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.ADM_VERIFY
        ret_arg = None
        out_msg = ''

        # Auto ADM operation (read from usim_modifier.xml)
        adm_code = arg_components.config.query_adm_code(
            arg_components.modeler.uicc.iccid)
        if adm_code == None:
            if arg_arguments == None:
                out_msg = res.get_string("input_adm_code")
            else:
                out_msg = arg_arguments
            print(layout_adm.layout(arg_msg=out_msg), end='')
            adm_code = input().strip().upper()

            if len(adm_code) == 0:
                ret_state = STATE.ERROR
                ret_arg = res.get_string("terminated_adm_code")
            elif not is_valid_adm_code(adm_code):
                ret_state = STATE.ADM
                ret_arg = res.get_string("invalid_adm_code")

        if ret_state == STATE.ADM_VERIFY:
            ret_arg = adm_code

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
