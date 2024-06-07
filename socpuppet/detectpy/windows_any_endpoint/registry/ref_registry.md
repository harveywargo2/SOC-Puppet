# Reg.exe - Registry Editor

The Windows registry is a centralized, hierarchical database that manages resources and stores configuration settings for applications on the Windows operating system. 
Security account services, user interfaces, and device drivers can all use the Windows registry.

**Registry keys** containers that act like folders, with values or subkeys contained within them.
**Registry values** are similar to files (not containers).

Registry Structure
- Hives: contain keys (directories) and values
- Keys: might contain subkeys and/or values
- Subkeys: no difference between key and subkey structure
- Values: store data

The main branches of the registry are called**hives**.
All the folders in the registry are called _keys_ except for the main hives.
- HKEY_CLASSES_ROOT (HKCR): 
  - This hive contains information about file associations, MIME types, and OLE (Object Linking and Embedding) object class registrations. 
  - It helps Windows determine which application should open a particular file type.
- HKEY_CURRENT_USER (HKCU): 
  - This hive stores configuration settings and preferences specific to the currently logged-in user. 
  - It includes desktop settings, program settings, and user-specific application preferences.
  - Ntuser.dat, Ntuser.dat.log
- HKEY_LOCAL_MACHINE (HKLM): 
  - This hive contains configuration settings and information for the local computer. 
  - It encompasses hardware configuration, software settings, and system-wide settings that apply to all users.
  - HKEY_LOCAL_MACHINE\SAM  
    - Sam, Sam.log, Sam.sav
  - HKEY_LOCAL_MACHINE\Security   
    - Security, Security.log, Security.sav
  - HKEY_LOCAL_MACHINE\Software   
    - Software, Software.log, Software.sav
  - HKEY_LOCAL_MACHINE\System
    - System, System.alt, System.log, System.sav
- HKEY_USERS (HKU): 
  - This hive contains subkeys for each user profile on the computer. 
  - Each user's settings are stored within their respective subkey.
  - Default, Default.log, Default.sav
- HKEY_CURRENT_CONFIG (HKCC): 
  - This hive contains information about the current hardware profile for the computer. 
  - It's primarily used during system startup.
  - System, System.alt, System.log, System.sav

The difference between HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER is 
- whether the referenced executable launches at startup for any user logging in
- or a specific user 
- (current_user is copied to a stored “user hive” and loaded whenever that user ID logs in)

## Ref Links
- Skill Up
  - https://medium.com/@nikhil.aniill/windows-registry-for-cybersecurity-beginners-63eebffb4049
  - https://www.avast.com/c-windows-registry
  - https://academy.tcm-sec.com/p/practical-windows-forensics
  - https://github.com/Defenders-Guide/TheDefendersGuide/blob/main/Windows/Windows%20Registry/The_Defenders_Guide_to_the_Windows_Registry.md