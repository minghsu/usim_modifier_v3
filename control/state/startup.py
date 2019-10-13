#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log


class startup():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "execute")

        layout = arg_components.viewer.get_layout(LAYOUT.STARTUP,
                                                  arg_name=arg_components.resource.get_string(
                                                      'app_name'),
                                                  arg_version=arg_components.resource.get_string(
                                                      'app_version'),
                                                  arg_copyright=arg_components.resource.get_string(
                                                      'copyright'))

        print(layout)

        return (STATE.INITIAL, None)
