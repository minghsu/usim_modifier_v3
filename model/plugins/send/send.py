#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString, toBytes
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc


class send(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    @property
    def is_update_require_adm(self):
        return None

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc
        if len(arg_arguments) != 0 and len(arg_arguments) % 2 != 1:
            print("TX: %s" % (toHexString(toBytes(arg_arguments))))
            response, sw1, sw2 = uicc.send(toBytes(arg_arguments))
            rx_resp = "%s %02X %02X" % (toHexString(response), sw1, sw2)
            print("RX: " + rx_resp.strip())

        log.debug(self.__class__.__name__, "EXIT")
