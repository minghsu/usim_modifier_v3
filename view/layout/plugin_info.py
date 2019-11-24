#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import view.layout.oneline as oneline
import control.resource as res

'''
  >>     '[plugin name]' loaded, version: V1.0, summary: Get and show the ATR value.
'''


def layout(arg_name='', arg_version='', arg_summary=''):
    ret_layout = ">> " + res.get_string('plugin_found') % (
        arg_name, arg_version, arg_summary)

    ret_layout = oneline.layout(arg_string=ret_layout, arg_padding=2)

    return ret_layout
