#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log
import control.resource as res


class plugin_list():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        print(res.get_string("plugin_loaded") %
              (len(arg_components.plugin)))

        for plugin in arg_components.plugin:
            print(arg_components.viewer.get_layout(LAYOUT.PLUGIN_INFO,
                                                   arg_name=plugin[0],
                                                   arg_version=plugin[1],
                                                   arg_summary=plugin[2]))
        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.CLI, None)
