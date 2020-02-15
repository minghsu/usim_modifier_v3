#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import view.layout.system.oneline as layout_oneline

'''
USIM modifier$
'''


def layout(arg_prefix=''):

    ret_layout = arg_prefix + '$ '

    ret_layout = layout_oneline.layout(
        arg_string=ret_layout, arg_style=STYLE.BRIGHT, arg_fore=COLOR_FORE.YELLOW)

    return ret_layout
