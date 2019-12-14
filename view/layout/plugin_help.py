#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import view.layout.oneline as oneline
import control.resource as res

'''

Help info of 'send' plugin
  Usage:
    - send XXXXXX

  Example of 'SELECT MF':
    - send 00A40004023F00
    > , 61 1F

'''


def layout(arg_name='', arg_help=''):

    ret_layout = os.linesep
    ret_layout += res.get_string('plugin_help_header') % (arg_name) + \
        os.linesep
    ret_layout += os.linesep

    lst_string = arg_help.split(os.linesep)
    for string in lst_string:
        ret_layout += oneline.layout(
            arg_string=string, arg_padding=2) + os.linesep

    return ret_layout
