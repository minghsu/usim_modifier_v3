#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
from control.components import components
from control.constants import LAYOUT, STATE
import control.log as log


class plugin():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        print(arg_components.resource.get_string(
            "plugin_loading"), end='')
        plugin_count = 0

        plugins_list = os.listdir("./model/plugins")
        for filename in plugins_list:
            name, ext = os.path.splitext(filename)
            if ext != '.py' and name != '__pycache__':
                try:
                    plugin_class = __import__("model.plugins.%s.%s" %
                                              (name, name), fromlist=[name])

                    res_files = [os.path.join(r, file) for r, d, f in os.walk(
                        './model/plugins/%s/values' % (name)) for file in f]
                    arg_components.resource.add_resource(name, res_files)

                    instance_class = getattr(plugin_class, name)()
                    plugin_count += 1
                except:
                    log.debug(self.__class__.__name__,
                              "Error to import '%s' plugin." % (name))

        print(arg_components.resource.get_string(
            "plugin_loaded") % (plugin_count))

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.EXIT, None)
