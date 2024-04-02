# CMSTP

Microsoft Connection Manager Profile Installer

## Common Attack TTPs
- Proxy Execution: 
  - Attackers might exploit cmstp.exe to execute malicious code by supplying it with infected .inf (installation information) files. These files can contain commands to load and run harmful programs on your system.
- Defense Evasion: 
  - Cmstp.exe, being a signed Microsoft application, may bypass certain security measures like AppLocker, making it harder to detect malicious activity.
- User Account Control (UAC) Bypass: 
  - In some scenarios, a malicious .inf file used with cmstp.exe could potentially bypass UAC, allowing the attacker to execute commands with elevated privileges.

## References Links
- LOLBAS: 
  - https://lolbas-project.github.io/lolbas/Binaries/Cmstp/
- MSFT Doc: 
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/ff961501(v=ws.11)
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmstp
- Research Write Up
  - https://oddvar.moe/2017/08/15/research-on-cmstp-exe/
  - https://medium.com/falconforce/falconfriday-detecting-uac-bypasses-0xff16-86c2a9107abf
- Pattern Examples:  
  - https://twitter.com/NickTyrer/status/958450014111633408
  - https://github.com/hfiref0x/UACME
  - https://gist.github.com/NickTyrer/bbd10d20a5bb78f64a9d13f399ea0f80
  - https://gist.github.com/api0cradle/cf36fd40fa991c3a6f7755d1810cc61e
  - https://gist.githubusercontent.com/tylerapplebaum/ae8cb38ed8314518d95b2e32a6f0d3f1/raw/3127ba7453a6f6d294cd422386cae1a5a2791d71/UACBypassCMSTP.ps1
- Open Source Detections
  - https://eqllib.readthedocs.io/en/latest/analytics/e584f1a1-c303-4885-8a66-21360c90995b.html
  - https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
  - https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
  - https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
- Mitre Attack
  - https://attack.mitre.org/techniques/T1218/003/

