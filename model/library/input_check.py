#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def is_valid_pin_code(arg_pincode):

    if len(arg_pincode) < 4 or len(arg_pincode) > 8:
        return False

    for i in range(len(arg_pincode)):
        if arg_pincode[i] not in "0123456789":
            return False

    return True

def is_valid_adm_code(arg_admcode):

    if len(arg_admcode) != 16:
        return False
    
    admcode = arg_admcode.upper()
    for i in range(len(admcode)):
        if admcode[i] not in "0123456789ABCDEF":
            return False

    return True    