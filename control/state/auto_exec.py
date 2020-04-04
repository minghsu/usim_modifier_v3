#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res


class auto_exec():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        if arg_components.config.autoexec:
            plugins = arg_components.plugin[:]
            for plugin in plugins:
                if plugin[4]:
                    plugin_class = __import__("model.plugins.%s.%s" %
                                            (plugin[0], plugin[0]), fromlist=[plugin[0]])
                    instance_class = getattr(plugin_class, plugin[0])()
                    instance_class.execute(arg_components, "")

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.HELP, None)
