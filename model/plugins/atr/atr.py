#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from smartcard.util import toHexString
from model.plugins.base_plugin import base_plugin
import control.log as log


class atr(base_plugin):
    def __init__(self):
        pass

    def summary(self):
        return "Displayed the value of Answer To Reset (ATR)."

    def version(self):
        return "1.00"

    @property
    def auto_execute(self):
        return False

    def execute(self, arg_connection, arg_parameter=""):
        log.debug(self.__class__.__name__, "ENTER")

        log.debug(self.__class__.__name__, "EXIT")
