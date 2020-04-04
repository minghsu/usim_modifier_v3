#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
from model.plugins.base_plugin import base_plugin


class cardinfo(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    @property
    def is_auto_exec(self):
        return True

    @property
    def is_update_require_adm(self):
        return True

    def execute(self, arg_components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        execute_list = ["iccid",
                        "imsi",
                        "mccmnc",
                        "spn",
                        "gid"]

        for plugin in execute_list:
            super(cardinfo, self).execute_plugin(plugin, arg_components)

        log.debug(self.__class__.__name__, "EXIT")
