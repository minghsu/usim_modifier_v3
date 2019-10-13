
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.modeler import modeler
from view.viewer import viewer
from control.resource import resource
from control.configuration import configuration
import control.log as log


class components:
    def __init__(self):
        self.__viewer = viewer()
        self.__config = configuration()
        self.__resource = resource(
            arg_localized=self.__config.localized)
        self.__modeler = modeler()

        log.init(arg_enable=self.__config.log)

    @property
    def modeler(self):
        return self.__modeler

    @property
    def viewer(self):
        return self.__viewer

    @property
    def resource(self):
        return self.__resource

    @property
    def config(self):
        return self.__config

    @property
    def log(self):
        return self.__logging
