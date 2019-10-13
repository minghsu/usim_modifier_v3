#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import STATE, LAYOUT
import control.log as log


class pin():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "execute")

        if arg_components.modeler.uicc.pin_enabled == True:
            print(arg_components.resource.get_string(
                "input_pin_code"), end='')

            pin_code = input().strip()
            if len(pin_code) == 0:
                pass
            if len(pin_code) >= 4 and len(pin_code) <= 8:
                pass

        print(pin_code)

        return (STATE.ADM, None)
