#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toASCIIBytes
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc
from model.library.convert import convert_arguments_to_dict
from control.constants import PIN_TYPE, ERROR
from model.library.input_check import is_valid_pin_code


class pin(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.01"

    @property
    def is_update_require_adm(self):
        return None

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        change_pin1_state_key = None
        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "pin1":
                change_pin1_state_key = value

        # change pin1 state
        if change_pin1_state_key != None:
            if is_valid_pin_code(change_pin1_state_key) == False:
                print(self.get_res("invalid_pin"))
            else:
                msg = None
                ret_result = None
                if uicc.pin_enabled:
                    ret_result, ret_retries = uicc.disable_pin(
                        toASCIIBytes(change_pin1_state_key))
                    msg = self.get_res(
                        'disable_ok') if ret_result == ERROR.NONE else self.get_res('disable_fail')
                else:
                    ret_result, ret_retries = uicc.enable_pin(
                        toASCIIBytes(change_pin1_state_key))
                    msg = self.get_res(
                        'enable_ok') if ret_result == ERROR.NONE else self.get_res('enable_fail')
                print(msg)
                if ret_result == ERROR.NONE and arg_components.config.query_pin_code(arg_components.modeler.uicc.iccid) != change_pin1_state_key:
                    arg_components.config.update_pin_code(
                        arg_components.modeler.uicc.iccid, change_pin1_state_key)

            print(os.linesep, end='')

        print(self.get_res("pin1").format(self.get_res("enable"),
                                          res.get_string("yes") if uicc.pin_enabled else res.get_string("no")))
        print(self.get_res("pin1").format(self.get_res("verify"),
                                          res.get_string("yes") if uicc.pin_verified else res.get_string("na")))

        ret_result, ret_retries = uicc.verify_pin(PIN_TYPE.PIN1, "")
        print(self.get_res("pin1").format(self.get_res("retries"), ret_retries))

        # space line
        print('')

        print(self.get_res("adm").format(self.get_res("verify"),
                                         res.get_string("yes") if uicc.adm_verified else res.get_string("no")))

        ret_result, ret_retries = uicc.verify_pin(PIN_TYPE.ADM1, "")
        print(self.get_res("adm").format(self.get_res("retries"), ret_retries))

        log.debug(self.__class__.__name__, "EXIT")
