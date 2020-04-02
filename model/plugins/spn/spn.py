#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString, toBytes
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc
from model.library.convert import convert_arguments_to_dict, convert_bcd_to_string, convert_string_to_bcd, convert_alpha_to_string
from control.constants import ERROR, UICC_FILE, UICC_SELECT_TYPE
from model.library.uicc_sel_resp import uicc_sel_resp


class spn(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        set_content = None
        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "set":
                set_content = value

        uicc_resp: uicc_sel_resp = uicc.select(
            UICC_FILE.SPN, arg_type=UICC_SELECT_TYPE.FROM_MF)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp != None:

            # 01 4D 49 4E 47 FF FF FF FF FF FF FF FF FF FF FF FF
            # First byte is 'display condition'
            # 2 to 17 is 'service provider name'
            print(self.get_res("original").format(convert_alpha_to_string(read_resp[1:]),
                                                    uicc_resp.length - 1,
                                                    toHexString(read_resp)))

            if set_content != None and self.is_update_require_adm == uicc.adm_verified:
                update_len = len(set_content)
                if update_len > (uicc_resp.length - 1):
                    update_len = (uicc_resp.length - 1)

                update_content = [0xFF] * uicc_resp.length
                update_content[0] = 0x01
                for i in range(update_len):
                    update_content[i+1] = ord(set_content[i])

                if uicc.update_binary(update_content) == ERROR.NONE:
                    print(self.get_res("updated").format(convert_alpha_to_string(update_content[1:]),
                                                            uicc_resp.length - 1,
                                                            toHexString(update_content)))
                else:
                    print(self.get_res("update_error"))

        else:
            print(self.get_res("read_error"))

        log.debug(self.__class__.__name__, "EXIT")
