#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.reader import reader
from model.uicc import uicc


class modeler:
    def __init__(self):
        self.__reader = reader()
        self.__uicc = None

    @property
    def reader(self):
        return self.__reader

    def uicc_initial(self):
        self.__uicc = uicc(self.reader.connection)

    @property
    def uicc(self):
        return self.__uicc
