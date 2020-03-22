# USIM Modifier Version 3.0

The 'usim midifier v3.0' is for modify your 'TEST USIM' card, you can modify the content of USIM card with PC/SC card reader on multi-platform (Windows/MAC/Linux).  
  
You can use this tool to do:
- Modify iccid/imsi/mccmnc/gid/spn for specific test
- Update msisdn to easy identify the USIM (Ex: Chunwau Telecom, FET NET, etc)
- Implement new plugin for your specific test (Such as 'Orange' plugin, you can configure 'TEST USIM' for Orange test case)

# Requirement Packages

- [python3](https://www.python.org/)
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

## Windows

N/A (I lost the install sequence, but 'usim_modifier v3' can works property on Windows platform, just need to install 'colorama' & 'pyscard' packages).

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
- mccmnc: Query or modify the value of MCC/MNC.
- imsi: Query or modify the value of IMSI.
- spn: Query or modify the value of SPN.
- atr: Get and show the ATR value.
- iccid: Query or modify the value of IMSI.
- msisdn: Query or modify the value of MSISDN
- send: Send the 'APDU' to USIM directly

You can type 'plugin' command to get all plugin info, the 'Update' column mean is able to modify in current session or not.  

![plugin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/plugin.png)

# Configure XML file

We can configure below items by 'usim_modifier.xml' file, you can use any text editor to enable/disable(1/0).

- log: turn on or turn off the loggin mechanism
- localized: force to use 'en_US' language resource
- pin: enable/disable auto store the 'pin code' to config file
- adm: enable/disable auto store the 'adm code' to config file

If you enabled the 'pin' or 'adm' auto store feature, it will store to 'usim_modifier.xml' file by plain text and support mutliple ICCID.

![config](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/config.png)

# Start to using 'usim_modifier_v3'

On 'Linux/Mac' OS, just type './usim_modifier.py' command.  
For 'Windows' OS, please type 'python3 usim_modifer.py' command.

The 1st step, if the USIM enabled the PIN code, you must nput correct 'pin code' to verify for future operation.  
For next step, you can type 'adm code' to verification 'adm', you can press 'ENTER' key to skip if you didn't have the 'adm code', but some 'plugin' may not updatable.  

PS. If the 'pin' & 'adm' verify success, we will store the 'pin' & 'adm' code to 'usim_modifier.xml' file automatically(can disable by 'usim_modifier.xml' file), and auto verification from next operation.

![startup](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/startup.png)
