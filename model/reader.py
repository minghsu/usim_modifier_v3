#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from smartcard.System import readers
from smartcard.Exceptions import NoCardException
from control.constants import ERROR


class reader:
    def __init__(self):
        self.__reader = None
        self.__connection = None
        cardreaders = readers()
        if len(cardreaders) > 0:
            self.__reader = cardreaders[0]

    @property
    def name(self):
        return self.__reader

    @property
    def connection(self):
        return self.__connection

    def close(self):
        if self.__connection != None:
            self.__connection.disconnect()
            self.__connection = None

    def open(self):
        try:
            self.__connection = self.__reader.createConnection()
            self.__connection.connect()
        except NoCardException:
            del self.__connection
            self.__connection = None
            return ERROR.CARD_ABSENT

        return ERROR.NONE
