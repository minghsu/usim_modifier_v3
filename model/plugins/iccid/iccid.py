#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString, toBytes
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc
from model.library.convert import convert_arguments_to_dict, convert_bcd_to_string, convert_string_to_bcd
from control.constants import ERROR, UICC_FILE, UICC_SELECT_TYPE
from model.library.uicc_sel_resp import uicc_sel_resp

class iccid(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    def help(self):
        ret_help = self.get_res("help")
        return ret_help % res.get_string("app_name")

    def get_res(self, arg_resid):
        return super(self.__class__, self).get_plugin_res(arg_resid)

    @property
    def auto_execute(self):
        return False

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc:uicc = arg_components.modeler.uicc

        update_iccid = False
        set_content = ""
        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "set":
                set_content = value
                update_iccid = True

        uicc_resp:uicc_sel_resp = uicc.select(UICC_FILE.ICCID, arg_type = UICC_SELECT_TYPE.FROM_MF)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp != None:
            print(self.get_res("original") %
                  (convert_bcd_to_string(read_resp),
                   toHexString(read_resp)))

            if update_iccid:
                original = convert_bcd_to_string(read_resp)
                update_content = set_content + original[len(set_content):]

                if uicc.update_binary(convert_string_to_bcd(update_content)) == ERROR.NONE:
                    print(self.get_res("updated") %
                          (update_content,
                           toHexString(convert_string_to_bcd(update_content))))
                else:
                    print(self.get_res("update_error"))

        else:
            print(self.get_res("read_error"))

        log.debug(self.__class__.__name__, "EXIT")
