#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc
from model.library.convert import convert_arguments_to_dict, convert_alpha_to_string, convert_dialing_number_to_string
from control.constants import ERROR, UICC_FILE, UICC_SELECT_TYPE
from model.library.uicc_sel_resp import uicc_sel_resp


class dir(base_plugin):
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

        uicc_resp: uicc_sel_resp = uicc.select(UICC_FILE.DIR)
        if uicc_resp.sw1 == 0x90:
            print("EF_DIR")
            for i in range(uicc_resp.count):
                resp = uicc.read_record(i+1, uicc_resp)
                if resp != None:
                    print("#{}: {}".format(i+1, toHexString(resp)))
        else:
            print(self.get_res("read_error"))

        log.debug(self.__class__.__name__, "EXIT")
