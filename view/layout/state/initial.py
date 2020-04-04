#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import view.layout.system.oneline as layout_oneline


def layout(arg_format='', arg_reader=''):

    out_msg = arg_format.format(arg_reader)
    ret_layout = layout_oneline.layout(arg_string=out_msg)

    return ret_layout
