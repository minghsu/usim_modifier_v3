# USIM Modifier Version 3.0

The 'usim midifier v3.0' is designed for modification your 'TEST USIM CARD', you can modify some data of USIM fileds with PC/SC card reader on multi-platform (Windows/MAC/Linux).  
  
Hope this tool can hlep you easy to create specific TEST USIM for test.

# Requirement Packages

- [colorama](https://pypi.org/project/colorama/)
- [pyscard](https://pyscard.sourceforge.io/)  
- [lxml](https://lxml.de/)  

# Prepare the environment

## Linux
> linux@ubuntu:/$ pip3 install colorama  
> linux@ubuntu:/$ sudo apt-get install swig  
> linux@ubuntu:/$ sudo apt-get install libpcsclite-dev  
> linux@ubuntu:/$ sudo pip3 install pyscard

## MAC OSX
> Pre-condition: “HomeBrew” must be installed.  
  
> mac@osx:/$ pip3 install colorama  
> mac@osx:/$ pip3 install lxml  
> mac@osx:/$ brew install swig  (PS. install “swig” by homebrew)  
> mac@osx:/$ pip3 install pyscard  

# Install "USIM modifier"

git clone https://github.com/minghsu/usim_modifier_v3.git

# Features

- Command Line Interface
- Multi-language with extendable architecture (plugin supported)
- Flexible plugin mechanism (you can implement that by self and planned to release tech note for develop)
- Auto verify 'pin' & 'adm' code (from usim_modifier.xml file)
- Auto store 'pin' & 'adm' code by ICCID (configurable)
- Logging support (configurable)

# Plugin supported features

- gid: Query or modify the value of GID1/GID2.
- mccmnc: Query or modify the value of MCC/MNC.
- imsi: Query or modify the value of IMSI.
- spn: Query or modify the value of SPN.
- atr: Get and show the ATR value.
- iccid: Query or modify the value of IMSI.
- msisdn: Query or modify the value of MSISDN
- send: Send the 'APDU' to USIM directly

![plugin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/plugin.png)

# Configure XML file

We can configure below items by 'usim_modifier.xml' file, you can use any text editor to enable/disable(1/0).

- log: turn on or turn off the loggin mechanism
- localized: force to use 'en_US' langueae resource
- pin: enable/disable auto store the 'pin code' to config file
- adm: enable/disable auto store the 'adm code' to config file

If you enabled the 'pin' or 'adm' auto store feature, it will store to 'usim_modifier.xml' file by plain text and support mutliple ICCID.

![plugin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/config.png)
