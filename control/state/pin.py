#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log

from smartcard.util import toASCIIBytes

from control.components import components
from control.constants import STATE, LAYOUT, ERROR, PIN_TYPE
from model.library.input_check import is_valid_pin_code

class pin():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "execute")

        if arg_components.modeler.uicc.pin_enabled == True:
            
            if arg_arguments == None:
                print(os.linesep)
                print(arg_components.resource.get_string(
                    "input_pin_code"), end='')
            else:
                print(arg_arguments, end='')
           
            pin_code = input().strip()

            if len(pin_code) == 0:
                return (STATE.ERROR, arg_components.resource.get_string(
                    "terminated_pin_code"))

            if not is_valid_pin_code(pin_code):
                return (STATE.PIN, arg_components.resource.get_string(
                    "invalid_pin_code"))

            verify_result, reamings = arg_components.modeler.uicc.verify_pin(PIN_TYPE.PIN1, toASCIIBytes(pin_code))
            if verify_result != ERROR.NONE:
                if reamings == 0:
                    return (STATE.ERROR, arg_components.resource.get_string(
                        "card_blocked"))
                else:
                    return (STATE.PIN, arg_components.resource.get_string(
                        "incorrect_pin_code") % (reamings))

        return (STATE.ADM, None)
