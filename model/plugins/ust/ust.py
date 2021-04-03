#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
import control.resource as res

from smartcard.util import toHexString, toBytes
from model.plugins.base_plugin import base_plugin
from control.components import components
from model.uicc import uicc
from model.library.convert import convert_arguments_to_dict, convert_bcd_to_string, convert_string_to_bcd
from control.constants import ERROR, UICC_FILE, UICC_SELECT_TYPE
from model.library.uicc_sel_resp import uicc_sel_resp


class ust(base_plugin):
    def __init__(self):
        pass

    def version(self):
        return "1.00"

    @property
    def is_update_require_adm(self):
        return None

    def execute(self, arg_components: components, arg_arguments=''):
        log.debug(self.__class__.__name__, "ENTER")

        uicc: uicc = arg_components.modeler.uicc

        # ETSI TS 131 102 V16.6.0 (2021-01)
        usim_service_table = [
            # 1
            "Local Phone Book",
            "Fixed Dialling Numbers(FDN)",
            "Extension 2",
            "Service Dialling Numbers(SDN)",
            "Extension 3",
            "Barred Dialling Numbers(BDN)",
            "Extension 4",
            "Outgoing Call Information(OCI and OCT)",
            "Incoming Call Information(ICI and ICT)",
            "Short Message Storage(SMS)",
            # 11
            "Short Message Status Reports(SMSR)",
            "Short Message Service Parameters(SMSP)",
            "Advice of Charge(AoC)",
            "Capability Configuration Parameters 2 (CCP2)",
            "Cell Broadcast Message Identifier",
            "Cell Broadcast Message Identifier Ranges",
            "Group Identifier Level 1",
            "Group Identifier Level 2",
            "Service Provider Name",
            "User controlled PLMN selector with Access Technology",
            # 21
            "MSISDN",
            "Image(IMG)",
            "Support of Localised Service Areas(SoLSA)",
            "Enhanced Multi-Level Precedence and Pre-emption Service",
            "Automatic Answer for eMLPP",
            "RFU",
            "GSM Access",
            "Data download via SMS-PP",
            "Data download via SMS-CB",
            "Call Control by USIM",
            # 31
            "MO-SMS Control by USIM",
            "RUN A T COMMAND command",
            "shall be set to '1'",
            "Enabled Services Table",
            "APN Control List(ACL)",
            "Depersonalisation Control Keys",
            "Co-operative Network List",
            "GSM security context",
            "CPBCCH Information",
            "Investigation Scan",
            # 41
            "MexE",
            "Operator controlled PLMN selector with Access Technology",
            "HPLMN selector with Access Technology",
            "Extension 5",
            "PLMN Network Name",
            "Operator PLMN List",
            "Mailbox Dialling Numbers",
            "Message W aiting Indication Status",
            "Call Forwarding Indication Status",
            "Reserved and shall be ignored",
            # 51
            "Service Provider Display Information",
            "Multimedia Messaging Service(MMS)",
            "Extension 8",
            "Call control on GPRS by USIM",
            "MMS User Connectivity Parameters",
            "Network's indication of alerting in the MS(NIA)",
            "VGCS Group Identifier List(EFVGCS and EFVGCSS)",
            "VBS Group Identifier List(EFVBS and EFVBSS)",
            "Pseudonym",
            "User Controlled PLMN selector for I-WLAN access",
            # 61
            "Operator Controlled PLMN selector for I-WLAN access",
            "User controlled WSID list",
            "Operator controlled WSID list",
            "VGCS security",
            "VBS security",
            "WLAN Reauthentication Identity",
            "Multimedia Messages Storage",
            "Generic Bootstrapping Architecture(GBA)",
            "MBMS security",
            "Data download via USSD and USSD application mode",
            # 71
            "Equivalent HPLMN",
            "Additional TERMINAL PROFILE after UICC activation",
            "Equivalent HPLMN Presentation Indication",
            "Last RPLMN Selection Indication",
            "OMA BCAST Smart Card Profile",
            "GBA-based Local Key Establishment Mechanism",
            "Terminal Applications",
            "Service Provider Name Icon",
            "PLMN Network Name Icon",
            "Connectivity Parameters for USIM IP connections",
            # 81
            "Home I-WLAN Specific Identifier List",
            "I-WLAN Equivalent HPLMN Presentation Indication",
            "I-WLAN HPLMN Priority Indication",
            "I-WLAN Last Registered PLMN",
            "EPS Mobility Management Information",
            "Allowed CSG Lists and corresponding indications",
            "Call control on EPS PDN connection by USIM",
            "HPLMN Direct Access",
            "eCall Data",
            "Operator CSG Lists and corresponding indications",
            # 91
            "Support for SM-over-IP",
            "Support of CSG Display Control",
            "Communication Control for IMS by USIM",
            "Extended Terminal Applications",
            "Support of UICC access to IMS",
            "Non-Access Stratum configuration by USIM",
            "PWS configuration by USIM",
            "RFU",
            "URI support by UICC",
            "Extended EARFCN support",
            # 101
            "ProSe",
            "USA T Application Pairing",
            "Media Type support",
            "IMS call disconnection cause",
            "URI support for MO SHORT MESSAGE CONTROL",
            "ePDG configuration Information support",
            "ePDG configuration Information configured",
            "ACDC support",
            "Mission Critical Services",
            "ePDG configuration Information for Emergency Service support",
            # 111
            "ePDG configuration Information for Emergency Service configured",
            "eCall Data over IMS",
            "URI support for SMS-PP DOWNLOAD as defined in 3GPP TS 31.111 [12]",
            "From Preferred",
            "IMS configuration data",
            "TV configuration",
            "3GPP PS Data Off",
            "3GPP PS Data Off Service List",
            "V2X",
            "XCAP Configuration Data",
            "EARFCN list for MTC/NB-IOT UEs",
            "5GS Mobility Management Information",
            "5G Security Parameters",
            "Subscription identifier privacy support",
            "SUCI calculation by the USIM",
            "UAC Access Identities support",
            "Expect control plane-based Steering of Roaming information during initial registration in VPLMN",
            "Call control on PDU Session by USIM"
        ]

        set_content = None
        dict_args = convert_arguments_to_dict(arg_arguments)
        for key, value in dict_args.items():
            if key == "set":
                set_content = value

        uicc_resp: uicc_sel_resp = uicc.select(UICC_FILE.UST)
        read_resp = uicc.read_binary(uicc_resp)
        if read_resp != None:
            print(self.get_res("original").format(toHexString(read_resp)))
            print("")
            for i in range(len(read_resp)):
                for j in range(8):
                    if read_resp[i] >> j & 1 == 1:
                        print(self.get_res("service").format(
                            i*8 + j + 1, usim_service_table[i*8 + j]))

        else:
            print(self.get_res("read_error"))

        log.debug(self.__class__.__name__, "EXIT")
