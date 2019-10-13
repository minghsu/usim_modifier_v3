#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from smartcard.util import toASCIIString, toHexString


def convert_bcd_to_string(bytes=[]):
    """Convert the BCD bytes array to string

    >>> vals = [0x98, 0x68, 0x00, 0x90, 0x91, 0x11, 0x09, 0x00, 0x10, 0x80]
    >>> convert_bcd_to_string(vals)
    '89860009191190000108'
    """
    ret_content = ""

    for i in range(0, len(bytes)):
        ret_content += str(bytes[i] & 0x0F) + str(bytes[i] >> 4)

    return ret_content


def convert_string_to_bcd(string=""):
    """Convert the string to BCD array

    >>> vals = "89860009191190000108"
    >>> convert_string_to_bcd(vals)
    [0x98, 0x68, 0x00, 0x90, 0x91, 0x11, 0x09, 0x00, 0x10, 0x80]
    """
    ret_len = int(len(string)/2) if (len(string) %
                                     2) == 0 else int(len(string)/2+1)
    ret_content = [0x00]*ret_len

    for i in range(len(string)):
        tmp = string[i*2:i*2+2]
        if len(tmp) == 2:
            ret_content[i] = (int(tmp[1]) * 16) + int(tmp[0])
        elif len(tmp) == 1:
            ret_content[i] = (ret_content[i] & 0xF0) + int(tmp[0])
        else:
            break

    return ret_content


def convert_alpha_to_string(bytes=[]):
    """Convert the bytes array of Alpha Identifier to string (Ex: ADN, EF_SPN)

    >>> vals = [0x4D, 0x41, 0x49, 0x20, 0x54, 0x45, 0x53, 0x54, 0xFF, 0xFF]
    >>> convert_alpha_to_string(vals)
    'MAI TEST'

    Todo: Should consider the SMS default 7-bit & UCS2 coding
    """

    ret_content = ""

    try:
        ret_content = toASCIIString(bytes[:bytes.index(0xFF)])
    except ValueError:
        ret_content = toASCIIString(bytes)

    return ret_content


def convert_dialing_number_to_string(bytes=[]):
    """Convert the bytes array of dialing number to string (Include TON_NPI byte)

    >>> vals = [0x81, 0x90, 0x82, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    >>> convert_dialing_number_to_string(vals)
    '0928000000'
    """
    ret_number = convert_bcd_to_string(bytes[1:bytes.index(0xFF)])
    if bytes[0] == 0x91:
        ret_number = "+" + ret_number

    return ret_number


def convert_arguments_to_dict(arguments=""):
    """Convert the argument to dict type

    >>> vals = name="super star" num="+12345678"
    >>> dict = { 'name': "super star",
                 'num': "+12345678"}

    """
    ret_dict = {}

    # Check the SPACE & EQ symbol position
    space_pos = arguments.find(' ')
    equal_pos = arguments.find('=')

    if equal_pos == -1:
        return ret_dict
    if (space_pos < equal_pos) and space_pos != -1:
        current_args = arguments[space_pos+1:]
    else:
        current_args = arguments[:]

    while (current_args.find("=") != -1):
        dict_value = None
        dict_key = None

        equal_pos = current_args.find('=')
        dict_key = current_args[:equal_pos]
        current_args = current_args[equal_pos+1:]
        if current_args[0] == '"':
            start_str_pos = 1
            end_str_pos = current_args[1:].find('"')
            if end_str_pos != -1:
                dict_value = current_args[start_str_pos:end_str_pos+1]
                current_args = current_args[end_str_pos+2:]
            else:
                break   # Can't found double quote sumbol, break
        else:
            start_str_pos = 0
            end_str_pos = current_args.find(' ')
            if end_str_pos != -1:
                dict_value = current_args[start_str_pos:end_str_pos]
                current_args = current_args[end_str_pos+1:]
            else:
                dict_value = current_args[start_str_pos:]
                current_args = ""

        if dict_key != None and dict_value != None:
            ret_dict[dict_key.lower().strip()] = dict_value

    return ret_dict
