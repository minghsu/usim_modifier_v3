#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.reader import reader
from model.uicc import uicc
from control.constants import ERROR

class modeler:
    def __init__(self):
        self.__reader = reader()
        self.__uicc = None

    @property
    def reader(self):
        return self.__reader

    @property
    def uicc(self):
        return self.__uicc

    def open(self):
        ret_val = self.__reader.open()
        if ret_val == ERROR.NONE:
            self.__uicc = uicc(self.reader.connection)
            if self.__uicc.initialed == False:
                ret_val = ERROR.CARD_INVALID
        return ret_val
    
    def close(self):
        self.__reader.close()
