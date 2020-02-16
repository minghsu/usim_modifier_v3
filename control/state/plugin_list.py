#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res
import view.layout.state.plugin_list as layout_plugin_list


class plugin_list():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        out_msg = layout_plugin_list.layout(arg_format=res.get_string('plugin_found'),
                                            arg_plugin=arg_components.plugin)
        print(out_msg)

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.CLI, None)