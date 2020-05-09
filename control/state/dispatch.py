#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res


class dispatch():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        ret_state = STATE.DISPATCH_ERROR
        ret_arguments = None

        log.debug(self.__class__.__name__, "ENTER")
        log.info(self.__class__.__name__, arg_arguments)

        lower_arguments = arg_arguments.lower()
        if (lower_arguments == 'plugin'):
            ret_state = STATE.PLUGIN_LIST
        elif (lower_arguments == 'help'):
            ret_state = STATE.HELP
        elif (lower_arguments == 'exit'):
            ret_state = STATE.EXIT
        elif (arg_arguments != ''):
            cmd_list = arg_arguments.split(' ')
            for plugin in arg_components.plugin:
                if (plugin[0] == cmd_list[0].lower()):
                    if (len(cmd_list) > 1 and 'help' == cmd_list[1].lower()):
                        ret_state = STATE.PLUGIN_HELP
                        ret_arguments = cmd_list[0]
                    else:
                        ret_state = STATE.EXECUTE
                        ret_arguments = cmd_list[0].lower() + " " + " ".join(cmd_list[1:])
                    break

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
