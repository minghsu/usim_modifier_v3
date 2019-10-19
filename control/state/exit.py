#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import STATE
import control.log as log


class exit():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        arg_components.modeler.close()

        log.debug(self.__class__.__name__, "EXIT")

        return (STATE.NONE, None)
