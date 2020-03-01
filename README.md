# USIM Modifier Version 3.0

I re-factor the software architecture and finished some popular plugins for USIM customization.
Please notice the customization feature is for 'TEST USIM', not comerical USIM.

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
- Flexible plugin mechanism
- Auto store 'pin' & 'adm' code by ICCID

# Supported Pugins

> - iccid: Display or modify the value of ICCID.
> - spn: Display or modify the value of SPN.
> - send: Send the APDU command to USIM directly
> - mccmnc: Display or modify the value of MCC/MNC.
> - atr: Displayed the value of Answer To Reset (ATR).
> - gid: Display or modify the value of GID1/GID2.
> - imsi: Display or modify the value of IMSI.

![plugin](https://github.com/minghsu/usim_modifier_v3/blob/master/docs/images/plugin.png)

# Misc

- The plugin is not back incompatible
- Will release 'user guide' & 'tech note' soon
