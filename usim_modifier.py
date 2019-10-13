#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from control.controller import controller
import colorama

if __name__ == "__main__":
    colorama.init()
    ctrl = controller()
    while (ctrl.do_job()):
        pass
