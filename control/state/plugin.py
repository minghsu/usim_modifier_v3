#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res
import view.layout.state.plugin as layout_plugin


class plugin():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        plugin_count = 0
        plugin = []

        plugins_list = os.listdir("./model/plugins")
        for filename in plugins_list:
            name, ext = os.path.splitext(filename)
            if ext != '.py' and name != '__pycache__' and name != '.DS_Store':
                try:
                    plugin_class = __import__("model.plugins.%s.%s" %
                                              (name, name), fromlist=[name])

                    res_files = [os.path.join(r, file) for r, d, f in os.walk(
                        './model/plugins/%s/values' % (name)) for file in f]
                    res.add_resource(name, res_files)

                    instance_class = getattr(plugin_class, name)()

                    if instance_class.summary() != None:
                        plugin_count += 1
                        plugin.append([name,
                                       instance_class.version(),
                                       instance_class.summary(),
                                       instance_class.is_update_require_adm,
                                       instance_class.is_auto_exec])

                except:
                    log.debug(self.__class__.__name__,
                              "Error to import '%s' plugin." % (name))

        arg_components.plugin = plugin
        out_msg = layout_plugin.layout(arg_format=res.get_string("plugin_loaded"),
                                       arg_count=plugin_count)
        print(out_msg)
        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.AUTO_EXEC, None)
