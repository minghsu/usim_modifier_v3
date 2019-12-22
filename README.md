# USIM Modifier Version 3.0

I just finished the system architecture, and decide to publish this repositorie first.

Current version only supportted few plugins due to I found some design issue, especially as 'layout'. 
I will focus to fix 'layout' part fisrt, then implement 'imsi', 'mccmnc', 'gid' & 'spn' plugins.
In my experience, the above 5 plugins should be covered most customization conditions

# New features

- Supported multi-language on 'plugin' layer
- Configurable for below features
> - Auto store 'pin' & 'adm' code by ICCID
> - Force UI to use 'English' language 
> - Disable the logging 

# Misc

- Old 'plugin' can't compatible with 'USIM modifier V3'.
- Only support 'atr', 'iccid' & 'send' plugins
