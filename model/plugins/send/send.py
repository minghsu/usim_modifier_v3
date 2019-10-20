#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log

from smartcard.util import toHexString, toBytes
from model.plugins.base_plugin import base_plugin


class send(base_plugin):
    def __init__(self):
        pass

    def summary(self):
        return "Send the APDU command to USIM directly"

    def version(self):
        return "1.00"

    def help(self):
        return ("Usage:\n"
                "  - send XXXXXX\n"
                "\n"
                "Example of 'SELECT MF':\n"
                "  - send 00A40004023F00\n"
                " > , 61 1F")

    @property
    def auto_execute(self):
        return False

    def execute(self):
        log.debug(self.__class__.__name__, "ENTER")

        log.debug(self.__class__.__name__, "EXIT")
