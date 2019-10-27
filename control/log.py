#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import logging
from datetime import datetime


def init(arg_enable=0):
    global log_enable
    
    log_enable = arg_enable

    if log_enable:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M:%S',
                            handlers=[logging.FileHandler(datetime.today().strftime("%Y%m%d-%H%M%S.log"), 'w', 'utf-8'), ])

def info(arg_tag, arg_message):
    if log_enable:
        logging.getLogger(arg_tag).info(arg_message)


def debug(arg_tag, arg_message):
    if log_enable:
        logging.getLogger(arg_tag).debug(arg_message)


def critical(arg_tag, arg_message):
    if log_enable:
        logging.getLogger(arg_tag).critical(arg_message)
