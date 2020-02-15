#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import traceback
import control.log as log
import control.resource as res

from control.components import components
from control.constants import STATE


class statemachine:
    def __init__(self,
                 arg_components: components,
                 arg_init_state=STATE.STARTUP):
        self.__components = arg_components
        self.__state = arg_init_state
        self.__arguments = None

    def exec(self):
        try:
            state_class = __import__("control.state.%s" %
                                     (self.__state), fromlist=[self.__state])
            state_instance = getattr(state_class, self.__state)()
            log.debug(self.__class__.__name__, self.__state)
            self.__state, self.__arguments = state_instance.execute(
                self.__components, self.__arguments)
        except Exception as e:
            error_class = e.__class__.__name__
            reason = e.args[0]
            cl, exc, tb = sys.exc_info()
            lastCallStack = traceback.extract_tb(tb)[-1]
            fileName = lastCallStack[0]
            lineNum = lastCallStack[1]
            # funcName = lastCallStack[2]

            errMsg = res.get_string("exception").format(
                os.path.basename(fileName), lineNum, reason)

            self.__state = STATE.EXCEPTION
            self.__arguments = errMsg

        if self.__state == STATE.NONE:
            return False

        return True
