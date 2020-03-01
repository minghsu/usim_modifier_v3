#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res
import view.layout.state.cli as layout_cli


class cli():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        ret_state = STATE.DISPATCH
        ret_arguments = None

        log.debug(self.__class__.__name__, "ENTER")

        out_msg = layout_cli.layout(arg_prefix=res.get_string('app_name'))
        print(out_msg, end='')
        ret_arguments = input().strip()

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
