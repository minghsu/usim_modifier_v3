#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import STATE
import control.log as log
import view.layout.state.error as layout_error


class error():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        out_msg = layout_error.layout(arg_string=arg_arguments)

        print(out_msg)
        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.EXIT, None)
