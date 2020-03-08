#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from smartcard.util import toBytes

from control.constants import ERROR, UICC_FILE, UICC_SELECT_TYPE


def select(arg_field, arg_type=UICC_SELECT_TYPE.FILE_ID):
    if len(arg_field) % 2:
        return None

    ret_cmd = [0x00] * int(len(arg_field) / 2 + 5)

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xA4  # INS
    ret_cmd[2] = arg_type  # P1
    ret_cmd[3] = 0x04  # P2, return FCP
    ret_cmd[4] = int(len(arg_field) / 2)  # LC
    ret_cmd[5:] = toBytes(arg_field.upper())

    return ret_cmd


def get_response(arg_length):
    ret_cmd = [0x00] * 5

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xC0  # INS
    ret_cmd[2] = 0x00  # P1
    ret_cmd[3] = 0x00  # P2
    ret_cmd[4] = arg_length  # Length

    return ret_cmd


def read_binary(arg_length):
    ret_cmd = [0x00] * 5

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xB0  # INS
    ret_cmd[2] = 0x00  # P1
    ret_cmd[3] = 0x00  # P2
    ret_cmd[4] = arg_length  # Length

    return ret_cmd


def update_binary(arg_content):
    ret_cmd = [0x00] * 5

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xD6  # INS
    ret_cmd[2] = 0x00  # P1
    ret_cmd[3] = 0x00  # P2
    ret_cmd[4] = len(arg_content)  # Length

    ret_cmd += arg_content

    return ret_cmd


def verify_pin(arg_type, arg_key):
    ret_cmd = [0xFF] * (5 + 8)

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0x20  # INS
    ret_cmd[2] = 0x00  # P1
    ret_cmd[3] = arg_type  # P2
    ret_cmd[4] = 0x08  # Length
    for i in range(len(arg_key)):
        ret_cmd[i+5] = arg_key[i]

    return ret_cmd


def read_record(arg_idx, arg_length):
    ret_cmd = [0x00] * 5

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xB2  # INS
    ret_cmd[2] = arg_idx  # arg_idx
    ret_cmd[3] = 0x04  # P2
    ret_cmd[4] = arg_length  # Length

    return ret_cmd


def update_record(arg_idx, arg_content):
    ret_cmd = [0x00] * 5

    ret_cmd[0] = 0x00  # CLA
    ret_cmd[1] = 0xDC  # INS
    ret_cmd[2] = arg_idx  # P1
    ret_cmd[3] = 0x04  # P2
    ret_cmd[4] = len(arg_content)  # Length

    ret_cmd += arg_content

    return ret_cmd
