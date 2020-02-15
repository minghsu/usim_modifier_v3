#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.constants import STYLE, COLOR_FORE


'''
  >>     '[plugin name]' loaded, version: V1.0, summary: Get and show the ATR value.
'''


def layout(arg_format='', arg_plugin=[]):
    ret_layout = ''
    for plugin in arg_plugin:
        ret_layout += "  >>" + \
            arg_format % (plugin[0], plugin[1], plugin[2]) + "\n"
    return ret_layout
