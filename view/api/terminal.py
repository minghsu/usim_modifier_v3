#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import unicodedata


def get_width():
    '''
    Returns a terminal width
    '''
    columns, rows = os.get_terminal_size()
    return columns


def get_string_display_width(arg_string):
    '''
    Returns a real display width of string
    '''
    return (sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in arg_string))
