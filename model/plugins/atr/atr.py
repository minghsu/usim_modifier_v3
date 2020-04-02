#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString
from model.plugins.base_plugin import base_plugin
from control.components import components


class atr(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    @property
    def is_update_require_adm(self):
        return None

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        print("ATR: {}".format(toHexString(arg_components.modeler.uicc.atr())))

        log.debug(self.__class__.__name__, "EXIT")
