#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import colorama


class PIN_TYPE:
    PIN1 = 0x01
    PIN2 = 0x81
    ADM1 = 0x0A


class ERROR:
    NONE = 0
    CARD_ABSENT = 1
    INVALID_ARGUMENT = 2
    INCORRECT_PIN = 3
    INCORRECT_ADM = 4
    UICC_BLOCKED = 5
    CARD_INVALID = 6
    UNKNOWN = 0x7F


class STATE:
    NONE = 'none'
    STARTUP = 'startup'
    INITIAL = 'initial'
    PIN_CODE = 'pin_code'
    PIN_VERIFY = 'pin_verify'
    ADM_CODE = 'adm_code'
    ADM_VERIFY = 'adm_verify'
    EXCEPTION = 'exception'
    ERROR = 'error'
    EXIT = 'exit'
    PLUGIN = 'plugin'
    CLI = 'cli'
    HELP = 'help'
    PLUGIN_LIST = 'plugin_list'
    EXECUTE = 'execute'
    DISPATCH = 'dispatch'
    DISPATCH_ERROR = 'dispatch_error'
    PLUGIN_HELP = 'plugin_help'
    AUTO_EXEC = 'auto_exec'


class UICC_FILE:
    MF = "3F00"
    ICCID = "2FE2"
    DIR = "2F00"
    ADF = "7FFF"
    IMSI = "7FFF6F07"
    AD = "7FFF6FAD"
    GID1 = "7FFF6F3E"
    GID2 = "7FFF6F3F"
    MSISDN = "7FFF6F40"
    SPN = "7FFF6F46"
    PNN = "7FFF6FC5"
    UST = "7FFF6F38"
    MFARR = "2F06"
    ADFARR = "7FFF6F06"


class UICC_SELECT_TYPE:
    FILE_ID = 0x00
    DF_NAME = 0x04
    FROM_MF = 0x08


class ALIGN:
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class STYLE:
    BRIGHT = colorama.Style.BRIGHT
    DIM = colorama.Style.DIM
    NORMAL = colorama.Style.NORMAL
    RESET_ALL = colorama.Style.RESET_ALL


class COLOR_FORE:
    BLACK = colorama.Fore.BLACK
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW
    BLUE = colorama.Fore.BLUE
    MAGENTA = colorama.Fore.MAGENTA
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE
    RESET = colorama.Fore.RESET


class COLOR_BACK:
    BLACK = colorama.Back.BLACK
    RED = colorama.Back.RED
    GREEN = colorama.Back.GREEN
    YELLOW = colorama.Back.YELLOW
    BLUE = colorama.Back.BLUE
    MAGENTA = colorama.Back.MAGENTA
    CYAN = colorama.Back.CYAN
    WHITE = colorama.Back.WHITE
    RESET = colorama.Back.RESET
