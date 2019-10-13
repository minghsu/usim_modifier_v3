#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.library.fcp import get_ef_file_type, get_pin_status, get_record_count, get_data_length


class uicc_sel_resp:
    def __init__(self, arg_resp, arg_sw1, arg_sw2):
        self.__resp = arg_resp
        self.__sw1 = arg_sw1
        self.__sw2 = arg_sw2

        self.__record_count = None
        self.__data_length = None
        self.__pin = None
        self.__ef_type = None

        if (self.__sw1 == 0x90):
            self.__pin = get_pin_status(self.__resp)
            self.__ef_type = get_ef_file_type(self.__resp)
            if self.__ef_type != None:
                self.__record_count = get_record_count(self.__resp)
                self.__data_length = get_data_length(self.__resp)

    @property
    def resp(self):
        return self.__resp

    @property
    def sw1(self):
        return self.__sw1

    @property
    def sw2(self):
        return self.__sw2

    @property
    def pin(self):
        return self.__pin

    @property
    def ef_type(self):
        return self.__ef_type

    @property
    def count(self):
        return self.__record_count

    @property
    def length(self):
        return self.__data_length
