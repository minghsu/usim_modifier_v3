# USIM Modifier Version 3.0

The 'usim midifier v3.0' is for modify your 'TEST USIM' card, you can modify the content of USIM card with PC/SC card reader on multi-platform (Windows/MAC/Linux).  
  
You can use this tool to do:
- Modify iccid/imsi/mccmnc/gid/spn for specific test
- Update msisdn to easy identify the USIM (Ex: Chunwau Telecom, FET NET, etc)
- Enable/disable the PIN1, and query the PIN1/ADM retry count

PS. If you have any suggestion, please raise the 'issues' or send mail to me directly.

# Update History

## 2025-04-27

- Todo: Update the task to fetch the AID value from the USIM application

## 2023-02-19

- Fixed: Handle MSISDN numbers with an odd number of digits correctly (Thanks for [Simon Arlott](https://github.com/nomis))

## 2021-05-30

- New: Add 'config' plugin to update 'usim_modifier.xml'

## 2021-05-15
- Fixed bug#3: Add 'admhex' option, value '1' is for hex, else are digits.
- Only accept 8(digits) or 16(hex) key length of adm.
- Enhance 'pin' plugin, will update the correct 'pin' code if auto save pin option enabled.

## 2021-04-12

- Fixed bug#4: Auto adm_verify did not stop when verify fail

## 2021-04-11
- New 'ust' plugin to display the 'USIM Service Table'.
- Modified the input condition of ADM key, it can accept 8 ~ 16 digits hexadecimal and auto fill 'FF' to 16-digit.

# Todo

- Update the task to fetch the AID value from the USIM applicationn (currently is query the 1st record from EF-DIR)

# Requirement Packages

- [python3](https://www.python.org/) (Minimum version is 3.6.x) 
- [colorama](https://pypi.org/project/colorama/)
- [pyscard](https://pyscard.sourceforge.io/)  
- [lxml](https://lxml.de/)  

# Prepare the environment

## Ubuntu 24.04 (tested with WSL2 & python3.12)
> linux@ubuntu:/$ sudo apt install python3-colorama (PS. should be installed by default)  
> linux@ubuntu:/$ sudo apt install python3-lxml  
> linux@ubuntu:/$ sudo apt install python3-pyscard

## Linux
> linux@ubuntu:/$ pip3 install colorama  
> linux@ubuntu:/$ pip3 install lxml  
> linux@ubuntu:/$ sudo apt-get install swig pcscd ibpcsclite-dev  
> linux@ubuntu:/$ sudo pip3 install pyscard

## MAC OSX
> Pre-condition: “HomeBrew” must be installed.  
  
> mac@osx:/$ pip3 install colorama  
> mac@osx:/$ pip3 install lxml  
> mac@osx:/$ brew install swig  (PS. install “swig” by homebrew)  
> mac@osx:/$ pip3 install pyscard  

## Windows

When I installed python 3.10 from Microsoft Store directly (PIP included) on Windows 11 22H2 (build: 22621.1105), and install colorama, lxml & pyscard packages directly, then 'usim_modifier_v3' can works fine.

PS. As my previous experience, we need to install some packages first for "pip install pyscard", if you encounter install fail at 'pyscard' package, please check the error message to install dependency package, then try again.

# Install "USIM modifier"

git clone https://github.com/minghsu/usim_modifier_v3.git

# Features

- Multiple platform supported (Windows/MAC/Linux)
- Multi-language with extendable architecture
- Flexible plugin mechanism
- Dedicated language resource for 'plugin' 
- Auto verify 'pin' & 'adm' code (from usim_modifier.xml file)
- Auto store 'pin' & 'adm' code by ICCID (configurable)
- Logging support (configurable)

# Plugin supported features

- gid: Query or modify the value of GID1/GID2.
- mccmnc: Query or modify the value of MCC/MNC
- imsi: Query or modify the value of IMSI
- spn: Query or modify the value of SPN
- atr: Get and show the ATR value
- iccid: Query or modify the value of IMSI
- msisdn: Query or modify the value of MSISDN
- send: Send the 'APDU' to USIM directly
- pin: Enable/disable PIN1 and query the retry count of PIN1/ADM
- ust: Display the 'USIM Service Table' features
- cardinfo: Show the 'iccid', 'imsi', 'mccmnc', 'spn' & 'gid' info

You can type 'plugin' command to get all plugin info, the 'Updatable' column mean is able to modify in current session or not, and the 'AutoExec' mean the plugin will auto execute during startup stage or not.  

![plugin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/plugin.png)

# Start to using 'usim_modifier_v3'

On 'Linux/Mac' OS, just type './usim_modifier.py' command.  
For 'Windows' OS, please type 'python3 usim_modifer.py' command.

The 1st step, if the USIM enabled the PIN code, you must input correct 'pin code' to verify for future operation.  
For next step, you can type 'adm code' to verification 'adm', and we can press 'ENTER' key to skip if you didn't have the 'adm code', but some 'plugin' may not updatable.  

![startup](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/startup.png)

# Example of plugins

All example are very simple, you can type 'help' argument to get more detail.

## ATR

![atr](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/atr.png)

## ICCID

![iccid](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/iccid.png)

## IMSI

![imsi](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/imsi.png)

## MCC/MNC

![mccmnc](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/mccmnc.png)

## SPN

![spn](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/spn.png)

## GID

![gid](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/gid.png)

## MSISDN

![msisdn](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/msisdn.png)

## PIN

![pin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/pin.png)

## UST (USIM Service Table)

![ust](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/ust.png)

## ARR

![arr](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/arr.png)

## DIR

![dir](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/dir.png)

## SEND

![send](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/send.png)

## CARDINFO

![cardinfo](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/cardinfo.png)

# Tech Note

Please refer [USIM Modifier V3 Tech Note](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/usim_modifier_v3_tech_note.pdf)

# Reference

- ETSI TS 102 221 - Smart Cards; UICC-Terminal interface; Physical and logical characteristics
- ETSI TS 131 102 - UMTS; LTE;Characteristics of the Universal Subscriber Identity Module (USIM) application
- ETSI TS 101 220 - Smart Cards; ETSI numbering system for telecommunication application providers
