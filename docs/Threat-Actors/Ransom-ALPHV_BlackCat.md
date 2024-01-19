# ALPHV-BlackCat Intel 
## SecurityScoreCard (CommandLine-Analysis-Pipe-IOC-TechAnalysis-Samples)
> https://securityscorecard.com/research/deep-dive-into-alphv-blackcat-ransomware/

Notes
- Privilege escalation via UAC bypass using CMSTPLUA COM interface

The LookupPrivilegeValueW routine is utilized to retrieve the locally unique identifier that represents the following privileges:
- SeIncreaseQuotaPrivilege SeSecurityPrivilege SeTakeOwnershipPrivilege 
- SeLoadDriverPrivilege SeSystemProfilePrivilege SeSystemtimePrivilege 
- SeProfileSingleProcessPrivilege SeIncreaseBasePriorityPrivilege 
- SeCreatePagefilePrivilege SeBackupPrivilege SeRestorePrivilege 
- SeShutdownPrivilege SeDebugPrivilege SeSystemEnvironmentPrivilege 
- SeChangeNotifyPrivilege SeRemoteShutdownPrivilege SeUndockPrivilege 
- SeManageVolumePrivilege SeImpersonatePrivilege SeCreateGlobalPrivilege 
- SeIncreaseWorkingSetPrivilege SeTimeZonePrivilege 
- SeCreateSymbolicLinkPrivilege SeDelegateSessionUserImpersonatePrivilege

The BlackCat configuration is stored in JSON form and is decrypted at runtime. It contains:
- the extension appended to the encrypted files 
- RSA public key that is used to encrypt the AES encryption key 
- ransom note name and content 
- stolen credentials specific to the victim’s environment 
- encryption cipher: AES 
- list of services and processes to be killed 
- list of folders, files, and extensions to be skipped 
- boolean values that indicate network discovery, lateral movement, setting the Desktop Wallpaper, killing VMware ESXi virtual machines, removing VMware ESXi virtual machine snapshots, excluding VMware ESXi virtual machines from termination


## MSFT (CommandLine-Tools-Alerts-Detections-IOC-Samples)
- https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)

Notes 
- Initial Access: remote desktop applications and compromised credentials
- Initial Access: Exchange server vulnerabilities
- Payload launches via dllhost.exe 
- BlackCat can bypass UAC, which means the payload will successfully run even if it runs from a non-administrator context
- BlackCat discovers all servers that are connected to a network. The process first broadcasts NetBIOS Name Service (NBNC) messages to check for these additional devices
- Attempts to replicate itself on the answering servers using the credentials specified within the config via PsExec.
- Using tools like Mimikatz 
- PsExec to deploy the ransomware payload
- Gathers Active Directory Info via ADFind & ADRecon
- Creates dump file of LSASS using Task Manager. Instead, they opened Taskmgr.exe, created a dump file of the LSASS.exe process, and saved the file to a ZIP archive.
- They used WMIC.exe using the previously gathered device name as the node, launched the command whoami /all, and pinged google.com to check network connectivity. The output of the results were then written to a .log file on the mounted share.
- Attackers attempted to navigate to various network shares and used the Remote Desktop client (mstsc.exe) to sign into these devices, once again using the compromised account credentials.
- Attackers used both MEGAsync and Rclone, which were renamed as legitimate Windows process names (for example, winlogon.exe, mstsc.exe).
- Attackers dropped and used ADFind.exe commands to gather information on persons, computers, organizational units, and trust information, as well as pinged dozens of devices to check connectivity.
- Used SMB to copy over and launch the Total Deployment Software administrative tool
- Total Deployment Software installed ScreenConnect
- Added a user account to the device using net.exe.
- The new user was then added to the local administrator group via net.exe.
- Exfiltrates data on devices they compromise from the organization using a malicious tool such as StealBit—often named “send.exe” or “sender.exe”. 


M365D AV/EDR
- Ransom:Win32/BlackCat!MSR
- Ransom:Win32/BlackCat.MK!MTB
- Ransom:Linux/BlackCat.A!MTB 
- An active ‘BlackCat’ ransomware was detected 
- ‘BlackCat’ ransomware was detected 
- BlackCat ransomware

## Varonic (CommandLine-IOC-TechAnalysis)
- https://www.varonis.com/blog/blackcat-ransomware

## Office of Information Security (Tools)
- https://www.hhs.gov/sites/default/files/royal-blackcat-ransomware-tlpclear.pdf

Tool List
- ADRecon 
- Cobalt Strike 
- PsExec 
- Mimikatz 
- Nirsoft 
- Emotet 
- ExMatter
- Bloodhound tool 
- Softperfect Netscan 
- CrackMapExec 
- Inveigh/InveighZero 
- MegaSync 
- Rclone 
- Adfind 
- Rubeus 
- Stealbit

## Palo Alto Unit 42 (Tools)
- https://unit42.paloaltonetworks.com/blackcat-ransomware/

Associated Tools
- Mimikatz
- LaZagne
- WebBrowserPassView
- GOST (Go Simple Tunnel)
- MEGASync
- Fileshredder

## IC3 (IOC-Samples)
- https://www.ic3.gov/Media/News/2022/220420.pdf

## Cyber Reason (CommandLine-IOC-Samples)
- https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware

Notes
- direct to ip callback to URL patterns

## Kaspersky 
- https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/06/23093553/Common-TTPs-of-the-modern-ransomware_low-res.pdf


## SOPHOS (TechAnalysis-Tools)
- https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck

Tools 
- Anydesk
- TeamViewer
- Cobalt Strike
- Brute Ratel
- DirLister
- PowerView
- Rsync
- MegaSync
- Netscan 
- Rclone


## Talos (Tools-CommandLine)
- https://blog.talosintelligence.com/from-blackmatter-to-blackcat-analyzing/

Tools
- Reverse SSH Tunnel
- Scheduled Tasks
- Gmer
- Browser Password Stealer
- Impacket
- ADRecon
- Powershell
- RDP
- PSEsec
- Softperfect Net Scanner
- HackBrowserData
- wsmprovhost.exe (WinRM)

## General 
- written in rust
- targets windows, linux & vmware
- Built-in privilege escalation (UAC bypass, Masquerade_PEB, CVE-2016-0099) 
- Can propagate to remote hosts via PsExec 
- Deletes shadow copies using VSS Admin
- Encryption algorithms: AES and ChaCha20