#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.components import components
from control.constants import LAYOUT, STATE, ERROR

import control.log as log
import control.resource as res


class initial():
    def __init__(self):
        pass

    def execute(self, arg_components: components, arg_arguments):
        log.debug(self.__class__.__name__, "ENTER")

        ret_state = STATE.EXIT
        ret_arguments = None
        if arg_components.modeler.reader.name == None:
            ret_state = STATE.ERROR
            ret_arguments = res.get_string("no_cardreader")
        else:
            ret = arg_components.modeler.open()
            if ret == ERROR.CARD_ABSENT:
                ret_state = STATE.ERROR
                ret_arguments = res.get_string("no_card")
            else:
                ret_state = STATE.PIN
                out_msg = res.get_string(
                    "reader_connected") % (arg_components.modeler.reader.name)
                out_msg = arg_components.viewer.get_layout(
                    LAYOUT.ONELINE, arg_string=out_msg)
                print(out_msg)

        log.debug(self.__class__.__name__, "EXIT")
        return (ret_state, ret_arguments)
