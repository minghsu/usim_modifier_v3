#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log
import control.resource as res


class cli():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        print(arg_components.viewer.get_layout(LAYOUT.CLI_PREFIX,
                                               arg_prefix=res.get_string('app_name')), end='')
        input().strip()

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.EXIT, None)
