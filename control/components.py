
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.modeler import modeler
from control.configuration import configuration

import control.log as log
import control.resource as res


class components:
    def __init__(self):
        self.__config = configuration()
        res.init(arg_localized=self.__config.localized)
        self.__modeler = modeler()
        self.__plugin = []

        log.init(arg_enable=self.__config.log)

    @property
    def plugin(self):
        return self.__plugin

    @plugin.setter
    def plugin(self, plugin):
        self.__plugin = plugin

    @property
    def modeler(self):
        return self.__modeler

    @property
    def config(self):
        return self.__config

    @property
    def log(self):
        return self.__logging
