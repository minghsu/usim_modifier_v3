#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# import all convert util from pyscard
from smartcard.util import *

import control.log as log
import control.resource as res
from model.plugins.base_plugin import base_plugin
from model.uicc import uicc
from control.components import components

# for response class of select USIM fields 
from model.library.uicc_sel_resp import uicc_sel_resp
# import all convert util from usim_modifier v3
from model.library.convert import *
# import all constants
from control.constants import *

class template(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    '''
    To configure your plugin is need ADM key or not
     - None: No update feature
     - True: Update need adm verified
     - False: Didn't need adm for update (ex: msisdn)
    '''
    @property
    def is_update_require_adm(self):
        return None

    '''
    To configure your plugin will auto exec during startup stage
     - True: Auto exec during startup
     - False: Don't need to auto exec
    '''
    @property
    def is_auto_exec(self):
        return False

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        '''
        ** Implement your code in here.

        In 'usim_modifier_v3' frameworks, just pass the arguments to plugin, 
        so you need to handle all operation by self, such as:

        1. select usim fields
        2. get input
        3. display message
        4. read data from usim
        5. update data to usim        


        ** Example of select usim filed
        
        # select MF
        uicc_resp: uicc_sel_resp = uicc.select(UICC_FILE.MF, arg_type=UICC_SELECT_TYPE.FILE_ID)

        # select other sim fields
        uicc_resp: uicc_sel_resp = uicc.select(UICC_FILE.ICCID)
        uicc_resp: uicc_sel_resp = uicc.select(UICC_FILE.IMSI)


        ** Execute other plugin
        
        super(template, self).execute_plugin(plugin_name, arg_components)
        '''
        print(self.get_res("hello"))

        log.debug(self.__class__.__name__, "EXIT")
