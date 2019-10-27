#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log
import control.resource as res


class startup():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        out_msg = arg_components.viewer.get_layout(LAYOUT.STARTUP,
                                                   arg_name=res.get_string(
                                                       'app_name'),
                                                   arg_version=res.get_string(
                                                       'app_version'),
                                                   arg_copyright=res.get_string(
                                                       'copyright'))

        print(out_msg)

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.INITIAL, None)
