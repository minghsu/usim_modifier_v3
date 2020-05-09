#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from control.constants import STYLE, COLOR_FORE
import view.layout.system.oneline as layout_oneline

'''

  Error Layout

'''


def layout(arg_string=''):

    ret_layout = os.linesep + layout_oneline.layout(
        arg_string=arg_string,
        arg_style=STYLE.BRIGHT,
        arg_fore=COLOR_FORE.RED,
        arg_padding=2)

    return ret_layout
