#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import control.resource as res
import view.layout.system.oneline as layout_oneline

'''

Help info of 'send' plugin
  Usage:
    - send XXXXXX

  Example of 'SELECT MF':
    - send 00A40004023F00
    > , 61 1F

'''


def layout(arg_format='', arg_name='', arg_help=''):

    ret_layout = os.linesep
    ret_layout += arg_format.format(arg_name) + os.linesep
    ret_layout += os.linesep

    lst_string = arg_help.split(os.linesep)
    for string in lst_string:
        ret_layout += layout_oneline.layout(
            arg_string=string, arg_padding=2) + os.linesep

    return ret_layout
