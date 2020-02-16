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
from control.constants import ERROR, UICC_FILE


class iccid(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    def help(self):
        ret_help = res.get_string("help", self.__class__.__name__)
        return ret_help % res.get_string("app_name")

    @property
    def auto_execute(self):
        return False

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        update_iccid = False
        set_content = ""
        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "set":
                set_content = value
                update_iccid = True

        read_resp = uicc.read_binary(UICC_FILE.ICCID)
        if read_resp != None:
            print("ICCID: %s (%s)" % (convert_bcd_to_string(
                read_resp), toHexString(read_resp)))

            if update_iccid:
                original = convert_bcd_to_string(read_resp)
                update_content = set_content + original[len(set_content):]

                if uicc.update_binary(convert_string_to_bcd(update_content)) == ERROR.NONE:
                    print("%s %s (%s)" % (res.get_string("updated", self.__class__.__name__),
                                          update_content,
                                          toHexString(convert_string_to_bcd(update_content))))
                else:
                    print(res.get_string("update_error", self.__class__.__name__))

        else:
            print(res.get_string("read_error", self.__class__.__name__))

        log.debug(self.__class__.__name__, "EXIT")