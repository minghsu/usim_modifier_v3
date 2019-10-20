#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib


class viewer:
    def __init__(self):
        self.__layout = {}
        layout_list = os.listdir("./view/layout")
        for filename in layout_list:
            name, ext = os.path.splitext(filename)
            if ext == '.py':
                self.__layout[name] = importlib.import_module(
                    'view.layout.' + name)

    def get_layout(self, arg_layout, **arg_kwargs):
        if arg_layout in self.__layout:
            return self.__layout[arg_layout].layout(**arg_kwargs)

        return ''
