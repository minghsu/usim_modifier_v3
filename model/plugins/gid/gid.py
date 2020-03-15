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


class gid(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        ID_GID1 = 0
        ID_GID2 = 1
        gid_working_list = [["GID1", UICC_FILE.GID1, None],
                            ["GID2", UICC_FILE.GID2, None]]

        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "gid1":
                gid_working_list[ID_GID1][2] = toBytes(value)
            elif key == "gid2":
                gid_working_list[ID_GID2][2] = toBytes(value)

        for i in range(len(gid_working_list)):
            uicc_resp: uicc_sel_resp = uicc.select(
                gid_working_list[i][1], arg_type=UICC_SELECT_TYPE.FROM_MF)
            read_resp = uicc.read_binary(uicc_resp)
            if read_resp != None:
                print(self.get_res("original") %
                      (gid_working_list[i][0],
                       toHexString(read_resp)))

                if gid_working_list[i][2] != None and self.is_update_require_adm == uicc.adm_verified:
                    update_content = read_resp[:]

                    update_len = len(gid_working_list[i][2])
                    if update_len > uicc_resp.length:
                        update_len = uicc_resp.length

                    for j in range(0, update_len):
                        update_content[j] = gid_working_list[i][2][j]

                    if uicc.update_binary(update_content) == ERROR.NONE:
                        print(self.get_res("updated") %
                              (gid_working_list[i][0],
                               toHexString(update_content)))
                    else:
                        print(self.get_res("update_error") %
                              (gid_working_list[i][0]))
            elif uicc_resp.sw1 == 0x6A and uicc_resp.sw1 == 0x82:
                print(self.get_res("not_exist") % (gid_working_list[i][0]))
            else:
                print(self.get_res("read_error") % (gid_working_list[i][0]))

        log.debug(self.__class__.__name__, "EXIT")
