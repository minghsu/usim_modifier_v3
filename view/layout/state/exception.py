#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import view.layout.system.oneline as layout_oneline

'''
  Exception, System terminated!!

    File: statemachine.py
    Line: 23
    Reason: No module named 'control.state.pin'
'''


def layout(arg_string=''):
    ret_layout = ""
    lst_string = arg_string.split(os.linesep)

    for string in lst_string:
        ret_layout += layout_oneline.layout(
            arg_string=string, arg_style=STYLE.BRIGHT, arg_fore=COLOR_FORE.RED, arg_padding=2) + os.linesep

    return ret_layout
