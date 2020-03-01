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

class mccmnc(base_plugin):
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

        uicc_resp:uicc_sel_resp = None
        uicc:uicc = None

        uicc = arg_components.modeler.uicc

        ori_mnc_length = None
        mnc_length = None
        efad_data_response = None

        set_mcc = ""
        set_mnc = ""
        update_mcc = False
        update_mnc = False

        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "mcc":
                set_mcc = value
                update_mcc = True
            elif key == "mnc":
                set_mnc = value
                update_mnc = True

        # Check the length of MCC/MNC
        if update_mcc and len(set_mcc) not in (0, 3):
            print(self.get_res("invalid_mcc"))
            return
        if update_mnc and len(set_mnc) not in (0, 2, 3):
            print(self.get_res("invalid_mnc"))
            return

        # read mnc length from EF_AD
        uicc_resp = uicc.select(UICC_FILE.AD, arg_type = UICC_SELECT_TYPE.FROM_MF)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp == None:
            print(self.get_res("read_error"))
            return

        efad_data_response = read_resp[:]   # keep for update mnc length
        ori_mnc_length = mnc_length = read_resp[3]
        # update mnc length to EF_AD if not equal
        if update_mnc and len(set_mnc) != mnc_length:
            mnc_length = len(set_mnc)
            efad_data_response[3] = mnc_length

            if uicc.update_binary(efad_data_response) != ERROR.NONE:
                print(self.get_res("update_error"))
                return

        # read EF_IMSI
        uicc_resp = uicc.select(UICC_FILE.IMSI, arg_type = UICC_SELECT_TYPE.FROM_MF)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp == None:
            print(self.get_res("read_error"))
            return

        mcc = convert_bcd_to_string(read_resp[1:])[1:4]
        mnc = convert_bcd_to_string(read_resp[1:])[4:4+ori_mnc_length]
        print(self.get_res("original") % (mcc, mnc))

        if update_mcc or update_mnc:
            update_imsi = read_resp[:]

            # prepare MCC
            if update_mcc and (len(set_mcc) == 3):
                update_imsi[1] = (
                    update_imsi[1] & 0x0F) + (int(set_mcc[0]) << 4)
                update_imsi[2] = (
                    update_imsi[2] & 0xF0) + (int(set_mcc[1]))
                update_imsi[2] = (
                    update_imsi[2] & 0x0F) + (int(set_mcc[2]) << 4)

            # prepare MNC
            if update_mnc and (len(set_mnc) >= 2):
                update_imsi[3] = (
                    update_imsi[3] & 0xF0) + (int(set_mnc[0]))
                update_imsi[3] = (
                    update_imsi[3] & 0x0F) + (int(set_mnc[1]) << 4)

                if len(set_mnc) == 3:
                    update_imsi[4] = (
                        update_imsi[4] & 0xF0) + (int(set_mnc[2]))

            if uicc.update_binary(update_imsi) != ERROR.NONE:
                print(self.get_res("update_error"))
                return

            mcc = convert_bcd_to_string(update_imsi[1:])[1:4]
            mnc = convert_bcd_to_string(update_imsi[1:])[4:4+mnc_length]
            print(self.get_res("updated") % (mcc, mnc))

        log.debug(self.__class__.__name__, "EXIT")
