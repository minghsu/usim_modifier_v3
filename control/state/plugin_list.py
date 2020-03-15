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

        plugins = arg_components.plugin[:]

        # check the ADM verify state
        # org: plugin name, version, is update adm require
        # new: plugin name, version, is updatable

        # is_update_require_adm:
        # - None: No update feature
        # - True: update need adm verified
        # - False: update didn't need adm verified
        for plugin in plugins:
            if plugin[3] == None:
                plugin[3] = "N/A"
            elif arg_components.modeler.uicc.adm_verified:
                plugin[3] = "Yes"
            else:
                plugin[3] = "Yes" if plugin[3] == arg_components.modeler.uicc.adm_verified else "No"

        out_msg = layout_plugin_list.layout(arg_format=res.get_string('plugin_found'),
                                            arg_plugin=plugins)
        print(out_msg)

        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.CLI, None)
