#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res


class execute():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        ret_state = STATE.CLI
        ret_arguments = None

        log.debug(self.__class__.__name__, "ENTER")
        log.info(self.__class__.__name__, arg_arguments)

        cmd_list = arg_arguments.split(" ")
        for plugin in arg_components.plugin:
            if (plugin[0] == cmd_list[0]):
                plugin_class = __import__("model.plugins.%s.%s" %
                                          (plugin[0], plugin[0]), fromlist=[plugin[0]])
                instance_class = getattr(plugin_class, plugin[0])()
                instance_class.execute(arg_components, " ".join(cmd_list[1:]))
                break

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
