#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.constants import STYLE
import view.layout.system.oneline as layout_oneline
import control.resource as res


def layout(arg_format='', arg_plugin=[]):

    # head line
    ret_layout = res.get_string("plugin_head").format(
        res.get_string("plugin_name"),
        res.get_string("plugin_version"),
        res.get_string("plugin_update"),
        res.get_string("plugin_autoexec"),
        res.get_string("plugin_summary")) + os.linesep

    ret_layout = layout_oneline.layout(
        arg_string=ret_layout, arg_style=STYLE.BRIGHT)

    for plugin in arg_plugin:
        ret_layout += res.get_string("plugin_item").format(
            plugin[0],
            plugin[1],
            plugin[3],
            plugin[4],
            plugin[2]) + os.linesep
    return ret_layout
