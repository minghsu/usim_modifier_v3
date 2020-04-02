#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
from importlib import util

import control.resource as res
from control.components import components

class base_plugin(abc.ABC):
    def summary(self):
        '''
        Returns a summary string by 'summary' resource key.
        If resource not defined 'help' key, will return 'None', and ignore that.
        '''
        ret_summary = res.get_string("summary", self.__class__.__name__)

        return ret_summary

    def help(self):
        '''
        Returns a help string by 'help' resource key.
        If resource not defined 'help' key, will call 'summary()' to instead it.
        '''
        ret_help = res.get_string("help", self.__class__.__name__)

        if ret_help == None:
            ret_help = self.summary()
        else:
            ret_help = ret_help.format(res.get_string("app_name"), self.__class__.__name__)
        return ret_help

    @abc.abstractmethod
    def version(self):
        return NotImplemented

    @abc.abstractmethod
    def execute(self, arg_components: components, arg_arguments=''):
        return NotImplemented

    # is update content need ADM verified
    @property
    def is_update_require_adm(self):
        return True

    @property
    def sort_index(self):
        return 0xFFFF

    def get_res(self, arg_resid):
        return res.get_string(arg_resid, self.__class__.__name__)

    def execute_plugin(self, arg_plugin_name, arg_components: components, arg_parameter=""):
        try:
            plugin_class = __import__("model.plugins.%s.%s" %
                                      (arg_plugin_name, arg_plugin_name), fromlist=[arg_plugin_name])
            instance_class = getattr(plugin_class, arg_plugin_name)()
            instance_class.execute(arg_components, arg_parameter)
        except:
            pass
