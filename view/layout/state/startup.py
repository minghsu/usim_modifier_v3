#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from control.constants import ALIGN

import view.api.terminal as terminal
import view.layout.system.oneline as layout_oneline

'''
****************************************************************
*                                                              *
*            USIM Modifier, ©Copyright 2019 Ming Hsu           *
*                                                              *
****************************************************************
'''


def layout(arg_name='', arg_version='', arg_copyright=''):

    width = terminal.get_width()

    ret_layout = ('*' * width) + os.linesep
    ret_layout += '*' + (' ' * (width-2)) + '*' + os.linesep

    app_title = "%s %s, %s" % (arg_name, arg_version, arg_copyright)
    ret_layout += layout_oneline.layout(arg_string=app_title,
                                        arg_align=ALIGN.CENTER,
                                        arg_padding=1,
                                        arg_padchar='*') + os.linesep

    ret_layout += '*' + (' ' * (width-2)) + '*' + os.linesep
    ret_layout += '*' * width

    return ret_layout
