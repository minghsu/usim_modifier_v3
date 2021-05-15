#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
from lxml import etree

CONFIG_XML_FILE = "usim_modifier.xml"


class configuration:
    def __init__(self):
        self.__xml = None
        if (self.load() == False):
            self.__default()
            self.save()

    def __default(self):
        self.__log = 0
        self.__localized = 1
        self.__pin = 1
        self.__adm = 1
        self.__autoexec = 1
        self.__admhex = 1

        root = etree.Element("usim_modifier")
        configuration = etree.SubElement(root, 'configuration')

        log = etree.SubElement(configuration, "log")
        log.text = str(self.__log)
        localized = etree.SubElement(configuration, "localized")
        localized.text = str(self.__localized)
        pin = etree.SubElement(configuration, "pin")
        pin.text = str(self.__pin)
        adm = etree.SubElement(configuration, "adm")
        adm.text = str(self.__adm)
        autoexec = etree.SubElement(configuration, "autoexec")
        autoexec.text = str(self.__autoexec)
        admhex = etree.SubElement(configuration, "admhex")
        admhex.text = str(self.__admhex)
        self.__xml = etree.ElementTree(root)

    def save(self):
        bRet = True
        try:
            self.__xml.write(CONFIG_XML_FILE, pretty_print=True,
                             xml_declaration=True, encoding='utf-8')
        except:
            log.critical(self.__class__.__name__,
                         "save usim_modifier.xml file fail.")
            bRet = False
        return bRet

    def update_pin_code(self, arg_iccid, arg_pin):
        root = self.__xml.getroot()
        uicc_node = root.xpath('//uicc[@iccid="' + arg_iccid + '"]')
        if len(uicc_node) == 0:
            uicc_node = etree.SubElement(
                root, 'uicc', attrib={'iccid': arg_iccid})
        else:
            uicc_node = uicc_node[0]

        pin_node = uicc_node.xpath('pin')
        if len(pin_node) == 0:
            pin_node = etree.SubElement(uicc_node, 'pin')
        else:
            pin_node = pin_node[0]

        if (pin_node.text != arg_pin):
            pin_node.text = arg_pin
            self.save()

    def query_pin_code(self, arg_iccid):
        ret_pin = None
        try:
            root = self.__xml.getroot()
            pin_node = root.xpath('//uicc[@iccid="' + arg_iccid + '"]/pin')
            if len(pin_node) > 0:
                return pin_node[0].text
        except Exception as e:
            log.info(self.__class__.__name__,
                     "Can't found the PIN of ICCID: " + arg_iccid)

        return ret_pin

    def update_adm_code(self, arg_iccid, arg_adm):
        root = self.__xml.getroot()
        uicc_node = root.xpath('//uicc[@iccid="' + arg_iccid + '"]')
        if len(uicc_node) == 0:
            uicc_node = etree.SubElement(
                root, 'uicc', attrib={'iccid': arg_iccid})
        else:
            uicc_node = uicc_node[0]

        adm_node = uicc_node.xpath('adm')
        if len(adm_node) == 0:
            adm_node = etree.SubElement(uicc_node, 'adm')
        else:
            adm_node = adm_node[0]

        if (adm_node.text != arg_adm):
            adm_node.text = arg_adm
            self.save()

    def query_adm_code(self, arg_iccid):
        ret_adm = None
        try:
            root = self.__xml.getroot()
            adm_node = root.xpath('//uicc[@iccid="' + arg_iccid + '"]/adm')
            if len(adm_node) > 0:
                return adm_node[0].text
        except Exception as e:
            log.info(self.__class__.__name__,
                     "Can't found the ADM of ICCID: " + arg_iccid)

        return ret_adm

    def load(self):
        bRet = True

        try:
            parser = etree.XMLParser(remove_blank_text=True)
            self.__xml = etree.parse(CONFIG_XML_FILE, parser)
            root = self.__xml.getroot()

            xml_node = root.xpath("configuration//log")
            self.__log = int(xml_node[0].text)
            xml_node = root.xpath("configuration//localized")
            self.__localized = int(xml_node[0].text)
            xml_node = root.xpath("configuration//pin")
            self.__pin = int(xml_node[0].text)
            xml_node = root.xpath("configuration//adm")
            self.__adm = int(xml_node[0].text)
            xml_node = root.xpath("configuration//autoexec")
            self.__autoexec = int(xml_node[0].text)
            xml_node = root.xpath("configuration//admhex")
            self.__admhex = int(xml_node[0].text)
        except Exception as e:
            print(e)
            log.critical(self.__class__.__name__,
                         "load usim_modifier.xml file fail.")
            bRet = False

        return bRet

    def __update_configurations(self, arg_key, arg_value):
        root = self.__xml.getroot()
        node = root.xpath('configuration//' + arg_key)
        if len(node) > 0:
            node[0].text = str(arg_value)
        else:
            log.critical(self.__class__.__name__,
                         "Can't update " + arg_key + " configuration, re-initial ...")
            self.__default()

        self.save()

    @property
    def autoexec(self):
        return self.__autoexec

    @autoexec.setter
    def autoexec(self, autoexec):
        self.__autoexec = autoexec
        self.__update_configurations('autoexec', self.__autoexec)

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log):
        self.__log = log
        self.__update_configurations('log', self.__log)

    @property
    def localized(self):
        return self.__localized

    @localized.setter
    def localized(self, localized):
        self.__localized = localized
        self.__update_configurations('localized', self.__localized)

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
        self.__update_configurations('pin', self.__pin)

    @property
    def adm(self):
        return self.__adm

    @adm.setter
    def adm(self, adm):
        self.__adm = adm
        self.__update_configurations('adm', self.__adm)

    @property
    def admhex(self):
        return self.__admhex

    @admhex.setter
    def admhex(self, admhex):
        self.__admhex = admhex
        self.__update_configurations('admhex', self.__admhex)
