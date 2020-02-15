#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from control.components import components
from control.constants import STATE
import control.log as log
import control.resource as res
import view.layout.state.help as layout_help


class help():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        out_msg = layout_help.layout(arg_help=res.get_string('help'))
        print(out_msg)
        log.debug(self.__class__.__name__, "EXIT")
        return (STATE.CLI, None)
