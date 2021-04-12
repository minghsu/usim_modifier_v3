#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import toASCIIBytes

from control.components import components
from control.constants import STATE, ERROR, PIN_TYPE
from model.library.input_check import is_valid_pin_code
import view.layout.state.pin_code as layout_pin_code


class pin_code():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.PIN_VERIFY
        ret_arg = None
        pin_code = None
        out_msg = ''

        if arg_components.modeler.uicc.pin_enabled == True:
            # if 'arg_arguments' exist, means may the auto verify fail.
            # so we can't read the pin code from .xml file
            if arg_arguments == None:
                # Auto PIN operation (read from usim_modifier.xml)
                pin_code = arg_components.config.query_pin_code(
                arg_components.modeler.uicc.iccid)
            
            if pin_code == None:
                if arg_arguments == None:
                    out_msg = res.get_string("input_pin_code")
                else:
                    out_msg = arg_arguments
                print(layout_pin_code.layout(arg_msg=out_msg), end='')
                pin_code = input().strip()

            if len(pin_code) == 0:
                ret_state = STATE.ERROR
                ret_arg = res.get_string("terminated_pin_code")
            elif not is_valid_pin_code(pin_code):
                ret_state = STATE.PIN_CODE
                ret_arg = res.get_string("invalid_pin_code")

            if ret_state == STATE.PIN_VERIFY:
                ret_arg = pin_code
        else:
            ret_state = STATE.ADM_CODE

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
