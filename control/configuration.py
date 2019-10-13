#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
from lxml import etree

CONFIG_XML_FILE = "usim_modifier.xml"


class configuration:
    def __init__(self):
        if (self.load() == False):
            self.__default()
            self.save()

    def __default(self):
        self.__log = 0
        self.__localized = 1
        self.__pin = 1
        self.__adm = 1

    def save(self):
        bRet = True

        try:
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

            tree = etree.ElementTree(root)
            tree.write(CONFIG_XML_FILE, pretty_print=True,
                       xml_declaration=True, encoding='utf-8')
        except:
            log.critical(self.__class__.__name__, "save usim_modifier.xml file fail.")
            bRet = False
        return bRet

    def query_pin_code(self, arg_iccid):
        ret_pin = None

        try:
            xml = etree.parse(CONFIG_XML_FILE)
            root = xml.getroot()

            pin_node = root.xpath('//uicc[@iccid="' + arg_iccid + '"]/pin')
            if len(pin_node) > 0:
                return pin_node[0].text

        except Exception as e:
            pass


        return ret_pin

    def load(self):
        bRet = True

        try:
            xml = etree.parse(CONFIG_XML_FILE)
            root = xml.getroot()

            xml_node = root.xpath("configuration//log")
            self.__log = int(xml_node[0].text)
            xml_node = root.xpath("configuration//localized")
            self.__localized = int(xml_node[0].text)
            xml_node = root.xpath("configuration//pin")
            self.__pin = int(xml_node[0].text)
            xml_node = root.xpath("configuration//adm")
            self.__adm = int(xml_node[0].text)
        except Exception as e:
            log.critical(self.__class__.__name__, "load usim_modifier.xml file fail.")
            bRet = False

        return bRet

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log):
        self.__log = log

    @property
    def localized(self):
        return self.__localized

    @localized.setter
    def localized(self, localized):
        self.__localized = localized

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def adm(self):
        return self.__adm

    @adm.setter
    def adm(self, adm):
        self.__adm = adm
