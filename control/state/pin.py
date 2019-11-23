#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import toASCIIBytes

from control.components import components
from control.constants import STATE, LAYOUT, ERROR, PIN_TYPE
from model.library.input_check import is_valid_pin_code


class pin():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.ADM
        ret_arg = None

        if arg_components.modeler.uicc.pin_enabled == True:
            auto_verify = False
            # Auto PIN operation (read from usim_modifier.xml)
            pin_code = arg_components.config.query_pin_code(
                arg_components.modeler.uicc.iccid)
            if arg_arguments == None and pin_code != None and is_valid_pin_code(pin_code):
                print(res.get_string(
                    "auto_pin_verifing") % (arg_components.modeler.uicc.iccid), end='')
                auto_verify = True
            else:
                if arg_arguments == None:
                    print(res.get_string("input_pin_code"), end='')
                else:
                    print(arg_arguments, end='')

                pin_code = input().strip()

                if len(pin_code) == 0:
                    ret_state = STATE.ERROR
                    ret_arg = res.get_string("terminated_pin_code")
                elif not is_valid_pin_code(pin_code):
                    ret_state = STATE.PIN
                    ret_arg = res.get_string("invalid_pin_code")

            if ret_arg == None:
                verify_result, reamings = arg_components.modeler.uicc.verify_pin(
                    PIN_TYPE.PIN1, toASCIIBytes(pin_code))

                if auto_verify == True:
                    if verify_result == ERROR.NONE:
                        print(res.get_string("pass"))
                    else:
                        print(res.get_string("fail"))

                # If enabled 'configuration.pin', store the pin code for auto verify
                if verify_result == ERROR.NONE and auto_verify != True:
                    if arg_components.config.pin == 1:
                        arg_components.config.update_pin_code(
                            arg_components.modeler.uicc.iccid, pin_code)

                if verify_result != ERROR.NONE:
                    if reamings == 0:
                        ret_state = STATE.ERROR
                        ret_arg = res.get_string("card_blocked")
                    else:
                        ret_state = STATE.PIN
                        ret_arg = res.get_string(
                            "incorrect_pin_code") % (reamings)

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
