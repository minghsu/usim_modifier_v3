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


class imsi(base_plugin):
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

        uicc_resp: uicc_sel_resp = None
        uicc: uicc = None

        uicc = arg_components.modeler.uicc

        set_content = None

        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "set":
                set_content = value

        # read EF_IMSI
        uicc_resp = uicc.select(
            UICC_FILE.IMSI, arg_type=UICC_SELECT_TYPE.FROM_MF)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp == None:
            print(self.get_res("read_error"))
            return

        # RAW IMSI: 08 09 10 10 10 32 54 76 98
        #              -  --------------------
        # Convert 09 10 10 10 32 54 76 98 => 9001010123456789
        # Ignore 1st char, and just use '001010123456789'
        print(self.get_res("original") % (convert_bcd_to_string(
            read_resp[1:])[1:], toHexString(read_resp)))

        if set_content != None:
            imsi_update_content = read_resp[:]

            for i in range(len(set_content)):
                if i == 15:
                    break
                Idx_of_PayLoad = int(((i + 1) / 2) + 1)
                Mod_Value = (i % 2)

                if Mod_Value == 0:
                    imsi_update_content[Idx_of_PayLoad] = (
                        imsi_update_content[Idx_of_PayLoad] & 0x0F) + (int(set_content[i]) << 4)
                else:
                    imsi_update_content[Idx_of_PayLoad] = (
                        imsi_update_content[Idx_of_PayLoad] & 0xF0) + int(set_content[i])

            if uicc.update_binary(imsi_update_content) != ERROR.NONE:
                print(self.get_res("update_error"))
                return

            print(self.get_res("updated") % (convert_bcd_to_string(
                imsi_update_content[1:])[1:], toHexString(imsi_update_content)))

        log.debug(self.__class__.__name__, "EXIT")
