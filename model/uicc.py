#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import control.log as log

from smartcard.util import toHexString

from model.apdu import select, get_response, read_binary, verify_pin
from model.library.uicc_sel_resp import uicc_sel_resp
from model.library.fcp import EF_FILE_TYPE
from model.library.convert import convert_bcd_to_string
from control.constants import ERROR, PIN_TYPE, UICC_FILE


class uicc:
    def __init__(self, arg_connection):
        self.__connection = arg_connection

        # check pin status
        self.__pin_verified = False
        self.__adm_verified = False
        self.__pin_enabled = False

        uicc_resp = self.select(UICC_FILE.MF)
        self.__pin_enabled = uicc_resp.pin

        self.__iccid = None
        read_resp = self.read_binary(UICC_FILE.ICCID)
        if read_resp != None:
            self.__iccid = convert_bcd_to_string(read_resp)
            log.info(self.__class__.__name__, "ICCID: " + self.__iccid)

    @property
    def iccid(self):
        return self.__iccid

    @property
    def pin_verified(self):
        return self.__pin_verified

    @property
    def pin_enabled(self):
        return self.__pin_enabled

    @property
    def adm_verified(self):
        return self.__adm_verified

    def __transmit(self, arg_apdu_cmd):
        log.debug(self.__class__.__name__,
                  "TX: %s" % (toHexString(arg_apdu_cmd)))
        response, sw1, sw2 = self.__connection.transmit(arg_apdu_cmd)
        log.debug(self.__class__.__name__,
                  "RX: %s, %02X %02X" % (toHexString(response), sw1, sw2))
        return (response, sw1, sw2)

    def atr(self):
        return self.__connection.getATR()

    def send(self, arg_apdu_cmd):
        return self.__transmit(arg_apdu_cmd)

    def select(self, arg_file_id):
        resp = sw1 = sw2 = None

        apdu = select(arg_file_id)
        if apdu != None:
            resp, sw1, sw2 = self.__transmit(apdu)

            if sw1 == 0x61:
                apdu = get_response(sw2)
                resp, sw1, sw2 = self.__transmit(apdu)

        return uicc_sel_resp(resp, sw1, sw2)

    def read_binary(self, arg_file_id):

        uicc_resp = self.select(arg_file_id)

        if uicc_resp.sw1 != 0x90 or uicc_resp.ef_type != EF_FILE_TYPE.TRANSPARENT:
            return None

        apdu = read_binary(uicc_resp.length)
        if apdu != None:
            resp, sw1, sw2 = self.__transmit(apdu)

            if sw1 == 0x90:
                return resp

        return None

    def verify_pin(self, arg_type, arg_code):
        ret_result = ERROR.NONE
        ret_reamings = None
        apdu = verify_pin(arg_type, arg_code)
        resp, sw1, sw2 = self.__transmit(apdu)

        if sw1 == 0x90:
            if arg_type == PIN_TYPE.PIN1:
                self.__pin_verified = True
            elif arg_type == PIN_TYPE.ADM1:
                self.__adm_verified = True

        if sw1 == 0x63:
            ret_reamings = sw2 & 0x0F
            if ret_reamings == 0:
                ret_result = ERROR.UICC_BLOCKED
            else:
                ret_result = ERROR.INCORRECT_PIN

        return (ret_result, ret_reamings)
