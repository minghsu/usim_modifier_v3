#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log
import control.resource as res


class execute():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        ret_state = STATE.CLI
        ret_arguments = None

        log.debug(self.__class__.__name__, "ENTER")

        cmd_list = arg_arguments.split(" ")
        for plugin in arg_components.plugin:
            if (plugin[0] == cmd_list[0]):
                plugin_class = __import__("model.plugins.%s.%s" %
                                          (plugin[0], plugin[0]), fromlist=[plugin[0]])

                instance_class = getattr(plugin_class, plugin[0])()
                if (len(cmd_list) > 1 and 'help' == cmd_list[1]):
                    print(arg_components.viewer.get_layout(LAYOUT.PLUGIN_HELP,
                                                           arg_name=cmd_list[0],
                                                           arg_help=instance_class.help()))
                    break
                else:
                    instance_class.execute(
                        arg_components, " ".join(cmd_list[1:]))

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
