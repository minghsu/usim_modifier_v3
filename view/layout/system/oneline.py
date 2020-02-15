#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.constants import ALIGN, STYLE, COLOR_FORE, COLOR_BACK
import view.api.terminal as terminal


def layout(arg_string='',
           arg_max_width=0,
           arg_align=ALIGN.LEFT,
           arg_style=STYLE.NORMAL,
           arg_fore=COLOR_FORE.RESET,
           arg_back=COLOR_BACK.RESET,
           arg_padding=0,
           arg_padchar=' '):
    '''
    Returns a string with style, color, align requirements

    @param arg_string: display string
    @param arg_max_width: base the width to operation, 0 mean to use width of terminal
    @param arg_align: left, center or right
    @param arg_style: normal, dim or bright
    @param arg_fore: foreground color
    @param arg_back: background color
    @param arg_padding: The padding size on left & right side
    @param arg_padchar: padding character
    '''

    ret_string = ''
    left_space = 0
    right_space = 0
    left_pading = ''
    right_pading = ''

    if arg_max_width == 0:
        width = terminal.get_width()
    else:
        width = arg_max_width

    if (arg_padding > 0):
        width -= (arg_padding * 2)
        left_pading = arg_padchar * arg_padding
        right_pading = arg_padchar * arg_padding

    str_width = terminal.get_string_display_width(arg_string)
    if arg_align == ALIGN.CENTER:
        reaming_space = width - str_width
        left_space = int(reaming_space/2)
        right_space = reaming_space - left_space
    elif arg_align == ALIGN.RIGHT:
        left_space = width - str_width
    elif arg_padding > 0:
        right_space = width - str_width

    ret_string += (' ' * left_space) + arg_string + \
        (' ' * right_space)

    ret_layout = (arg_style + arg_fore + arg_back + left_pading +
                  ret_string + right_pading + STYLE.RESET_ALL)

    return ret_layout
