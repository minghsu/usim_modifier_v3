#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import STATE
from control.statemachine import statemachine


class controller:
    def __init__(self):
        self.__components = components()
        self.__state = statemachine(self.__components)

    def do_job(self):
        return self.__state.exec()
