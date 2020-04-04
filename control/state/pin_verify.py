#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import control.log as log
import control.resource as res

from smartcard.util import toASCIIBytes

from control.components import components
from control.constants import STATE, ERROR, PIN_TYPE
from model.library.input_check import is_valid_pin_code


class pin_verify():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.ADM_CODE
        ret_arg = None

        verify_result, reamings = arg_components.modeler.uicc.verify_pin(
            PIN_TYPE.PIN1, toASCIIBytes(arg_arguments))

        # If enabled 'configuration.pin', store the pin code for auto verify
        if verify_result == ERROR.NONE:
            arg_components.modeler.uicc.pin_verified = True
            if arg_components.config.pin == 1:
                arg_components.config.update_pin_code(
                    arg_components.modeler.uicc.iccid, arg_arguments)
        else:
            if reamings == 0:
                ret_state = STATE.ERROR
                ret_arg = res.get_string("card_blocked")
            else:
                ret_state = STATE.PIN_CODE
                ret_arg = res.get_string("incorrect_pin_code").format(reamings)

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arg)
