#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
from importlib import util


class base_plugin(abc.ABC):
    @abc.abstractmethod
    def summary(self):
        return NotImplemented

    @abc.abstractmethod
    def version(self):
        return NotImplemented

    @abc.abstractmethod
    def execute(self, arg_connection):
        return NotImplemented

    @property
    def auto_execute(self):
        return False

    @property
    def sort_index(self):
        return 0xFFFF

    def help(self):
        return self.summary()

    def execute_plugin(self, arg_plugin_name, arg_connection, arg_parameter=""):

        ret_content = None
        try:
            plugin_class = __import__("model.plugins.%s.%s" %
                                      (arg_plugin_name, arg_plugin_name), fromlist=[arg_plugin_name])
            instance_class = getattr(plugin_class, arg_plugin_name)()
            ret_content = instance_class.execute(arg_connection, arg_parameter)
        except:
            pass

        return ret_content
