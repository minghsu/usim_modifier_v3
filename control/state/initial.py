#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import LAYOUT, STATE, ERROR
import control.log as log


class initial():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        ret_state = STATE.EXIT
        ret_arguments = None
        log.debug(self.__class__.__name__, "execute")

        if arg_components.modeler.reader.name == None:
            ret_state = STATE.ERROR
            ret_arguments = arg_components.resource.get_string(
                "no_cardreader")
        else:
            ret = arg_components.modeler.open()
            if ret == ERROR.CARD_ABSENT:
                ret_state = STATE.ERROR
                ret_arguments = arg_components.resource.get_string(
                    "no_card")
            else:
                ret_state = STATE.PIN
                layout = arg_components.resource.get_string(
                    "reader_connected") % (arg_components.modeler.reader.name)
                layout = arg_components.viewer.get_layout(
                    LAYOUT.ONELINE, arg_string=layout)
                print(layout)

        return (ret_state, ret_arguments)
