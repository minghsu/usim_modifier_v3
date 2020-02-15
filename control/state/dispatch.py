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
        ret_state = STATE.CLI
        ret_arguments = None

        log.debug(self.__class__.__name__, "ENTER")
        log.info(self.__class__.__name__, arg_arguments)

        if (arg_arguments == 'plugin'):
            ret_state = STATE.PLUGIN_LIST
        elif (arg_arguments == 'help'):
            ret_state = STATE.HELP
        elif (arg_arguments == 'exit'):
            ret_state = STATE.EXIT
        elif (arg_arguments != ''):
            cmd_list = arg_arguments.split(' ')
            for plugin in arg_components.plugin:
                if (plugin[0] == cmd_list[0]):
                    ret_state = STATE.EXECUTE
                    ret_arguments = arg_arguments
                    break

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
