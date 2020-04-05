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


class msisdn(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    @property
    def is_update_require_adm(self):
        return False

    def show_record(self, arg_idx, arg_resp, arg_name_len):
        '''
        The length of the 'name' should not a fixed, so ...
        '''
        name_str = convert_alpha_to_string(arg_resp[:arg_name_len])
        name_str += " " * (arg_name_len - len(name_str))

        num_str = convert_dialing_number_to_string(
            arg_resp[arg_name_len+1:arg_name_len+1+11])
        num_str += " " * (21 - len(num_str))

        print(self.get_res("record").format(arg_idx, name_str,
                                            arg_name_len, num_str, toHexString(arg_resp)))
        print("")

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        set_record_id = None
        set_name_content = None
        set_num_content = None

        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "id":
                set_record_id = int(value)
            elif key == "name":
                set_name_content = value
            elif key == "num":
                set_num_content = value

        uicc_resp: uicc_sel_resp = uicc.select(
            UICC_FILE.MSISDN, arg_type=UICC_SELECT_TYPE.FROM_MF)

        if uicc_resp.sw1 == 0x90:
            if set_record_id != None and (set_record_id <= 0 or set_record_id > uicc_resp.count):
                print(self.get_res("invalid_id"))
            else:
                name_length = uicc_resp.length - 14
                print(self.get_res("original"))
                for i in range(uicc_resp.count):
                    resp = uicc.read_record(i+1, uicc_resp)
                    if resp != None:
                        self.show_record(i+1, resp, name_length)

                if set_record_id != None and set_num_content != None and set_name_content != None:
                    update_apdu = uicc.read_record(set_record_id, uicc_resp)

                    if set_name_content != None:
                        # Name
                        update_name_len = len(set_name_content)
                        for i in range(name_length):
                            if i < update_name_len:
                                update_apdu[i] = ord(set_name_content[i])
                            else:
                                update_apdu[i] = 0xFF

                    if set_num_content != None:
                        # Num Length
                        if len(set_num_content) % 2 == 1:
                            update_apdu[name_length] = int(
                                len(set_num_content)/2) + 1
                        else:
                            update_apdu[name_length] = int(
                                len(set_num_content)/2)

                        # Num: BCD 10 (20 digits) + TON NPI
                        if update_apdu[name_length] > 11:
                            update_apdu[name_length] = 11

                        # '+' symbol
                        if len(set_num_content) > 0 and set_num_content[0] == "+":
                            update_apdu[name_length+1] = 0x91
                            set_num_content = set_num_content[1:]
                        else:
                            update_apdu[name_length+1] = 0x81

                        # Reset Number to 0xFF
                        for i in range(10):
                            update_apdu[name_length+1+1+i] = 0xFF

                        update_num_len = len(set_num_content)
                        if update_num_len > 20:
                            update_num_len = 10

                        num_apdu_index = name_length+1+1
                        for i in range(update_num_len):
                            tmp = set_num_content[i*2:i*2+2]
                            if len(tmp) == 2:
                                update_apdu[num_apdu_index +
                                            i] = (int(tmp[1]) * 16) + int(tmp[0])
                            elif len(tmp) == 1:
                                update_apdu[num_apdu_index+i] = (
                                    update_apdu[num_apdu_index+i] & 0xF0) + int(tmp[0])

                    if uicc.update_record(set_record_id, update_apdu) == ERROR.NONE:
                        print(self.get_res("updated"))
                        self.show_record(
                            set_record_id, update_apdu, name_length)
                    else:
                        print(self.get_res("update_error"))
        else:
            print(self.get_res("read_error"))

        log.debug(self.__class__.__name__, "EXIT")
