#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res
import view.layout.state.plugin_help as layout_plugin_help


class plugin_help():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        out_msg = layout_plugin_help.layout(arg_format=res.get_string('plugin_help_header'),
                                            arg_name=arg_arguments[0],
                                            arg_help=arg_arguments[1])

        print(out_msg)
        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.CLI, None)
