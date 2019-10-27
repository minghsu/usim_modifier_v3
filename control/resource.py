#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import locale

from lxml import etree

DEF_RES_DEFAULT_TAG = 'default'
DEF_RES_NO_VALUE = None

'''
The '__values' will contain all resource for 'usim_modifier_v3',
include 'system' & all 'plugin' resource.

The architecture is similar below:

self.__values = {
    {'system': 
        {'zh_TW': {'not_defined': '未定義的字串資源', 
                    'app_name': 'USIM 修改員', 
                    'version': '版本', 
                    'copyright': 'Copyright© 2019 許志銘'}, 
         'default': {'app_version': '3.0', 
                     'not_defined': 'This string was not defined', 
                     'app_name': 'USIM Modifier', 
                     'version': 'Version', 
                     'copyright': 'Copyright© 2019 Ming Hsu'}
        }
    },
    {'imsi': 
        {'zh_TW': {},
         'default': {}
        }
    }
}
'''


def init(arg_localized):
    global res_localized
    global res_locale
    global res_values

    res_localized = arg_localized
    res_locale = locale.getdefaultlocale()[0]
    res_values = {}

    system_res_files = [os.path.join(r, file) for r, d, f in os.walk(
        './control/values') for file in f]

    add_resource('system', system_res_files)

def add_resource(arg_tag, arg_files):
    '''
    Parse the xml files and add to resource center

    @param arg_tag: Resource tag for the string.

    @param arg_files: A list of full xml pathnames to initial string resource
    '''

    prepare_resource = {}
    for filename in arg_files:
        name, ext = os.path.splitext(os.path.basename(filename))

        if res_localized == 0 and name != 'default':
            continue

        tmp_resource_string = {}
        tmp_xml = etree.parse(
            filename, parser=etree.XMLParser(encoding='utf-8')).getroot()
        values = tmp_xml.xpath("string")
        for value in values:
            tmp_resource_string[value.attrib['name']] = value.text
        prepare_resource[name] = tmp_resource_string

    res_values[arg_tag] = prepare_resource

def get_string(arg_res_key, arg_source='system'):
    '''
    Returns a localized string from the system's or plugin's string table.

    @param arg_key: Resource key for the string.

    @param arg_source: Return from system's or plugin's (by plugin name) string table.

    Return "" string if can't found the resource key.
    '''
    if arg_source in res_values:
        resrouce_source = res_values[arg_source]

        if res_locale in resrouce_source:
            resource_target = resrouce_source[res_locale]

            if arg_res_key in resource_target:
                return resource_target[arg_res_key]

        # locale resource not include the arg_res_key
        if DEF_RES_DEFAULT_TAG in resrouce_source:
            resource_target = resrouce_source[DEF_RES_DEFAULT_TAG]
            if arg_res_key in resource_target:
                return resource_target[arg_res_key]

    return DEF_RES_NO_VALUE
