#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# import all convert util from pyscard
from smartcard.util import *

import control.log as log
import control.resource as res
from model.plugins.base_plugin import base_plugin
from model.uicc import uicc
from control.components import components

# for response class of select USIM fields
from model.library.uicc_sel_resp import uicc_sel_resp
# import all convert util from usim_modifier v3
from model.library.convert import *
# import all constants
from control.constants import *


class config(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    '''
    To configure your plugin is need ADM key or not
     - None: No update feature
     - True: Update need adm verified
     - False: Didn't need adm for update (ex: msisdn)
    '''
    @property
    def is_update_require_adm(self):
        return None

    '''
    To configure your plugin will auto exec during startup stage
     - True: Auto exec during startup
     - False: Don't need to auto exec
    '''
    @property
    def is_auto_exec(self):
        return False

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        update_log = None
        update_localized = None
        update_pin = None
        update_adm = None
        update_autoexec = None
        update_admhex = None

        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "log":
                update_log = int(value)
            elif key == "localized":
                update_localized = int(value)
            elif key == "pin":
                update_pin = int(value)
            elif key == "adm":
                update_adm = int(value)
            elif key == "autoexec":
                update_autoexec = int(value)
            elif key == "admhex":
                update_admhex = int(value)

        if update_log != None:
            arg_components.config.log = update_log
        if update_localized != None:
            arg_components.config.localized = update_localized
        if update_pin != None:
            arg_components.config.pin = update_pin
        if update_adm != None:
            arg_components.config.adm = update_adm
        if update_autoexec != None:
            arg_components.config.autoexec = update_autoexec
        if update_admhex != None:
            arg_components.config.admhex = update_admhex

        if update_log != None or update_localized != None or update_pin != None or update_adm != None or update_autoexec != None or update_admhex != None:
            arg_components.config.save()

        print(self.get_res("log").format(res.get_string("yes")
              if arg_components.config.log == 1 else res.get_string("no")))

        print(self.get_res("localized").format(res.get_string("yes")
              if arg_components.config.localized == 1 else res.get_string("no")))

        print(self.get_res("pin").format(res.get_string("yes")
              if arg_components.config.pin == 1 else res.get_string("no")))

        print(self.get_res("adm").format(res.get_string("yes")
              if arg_components.config.adm == 1 else res.get_string("no")))

        print(self.get_res("autoexec").format(res.get_string("yes")
              if arg_components.config.autoexec == 1 else res.get_string("no")))

        print(self.get_res("admhex").format(res.get_string("yes")
              if arg_components.config.admhex == 1 else res.get_string("no")))

        log.debug(self.__class__.__name__, "EXIT")
