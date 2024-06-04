# gsecdump

## References
- Mitre 
  - https://attack.mitre.org/software/S0008/
- Intel Links
  - https://infra.newerasec.com/infrastructure-testing/privilege-esclation/password-dumping
  - http://www.malos-ojos.com/wp-content/uploads/2010/05/Windows_Hash_Reinjection.pdf
  - https://dmcxblue.gitbook.io/red-team-notes/untitled-1/credential-dumping
  - https://dmcxblue.gitbook.io/red-team-notes/untitled-1/credential-dumping
- MDE AV Info 
  - https://www.microsoft.com/en-us/wdsi/threats/threat-search?query=GSECDump
  - HackTool:Win32/Gsecdump
  - HackTool:Win64/Gsecdump
  - HackTool:Win32/Gsecdump!pz
- Tool Location
  - https://download.openwall.net/pub/projects/john/contrib/win32/pwdump/gsecdump-0.7-win32.zip
  - https://web.archive.org/web/20150606043951if_/http://www.truesec.se/Upload/Sakerhet/Tools/gsecdump-v2b5.exe
- Analysis
  - https://www.hybrid-analysis.com/sample/94cae63dcbabb71c5dd43f55fd09caeffdcd7628a02a112fb3cba36698ef72bc/5a7dfcf57ca3e10d6a0b53e3
  - https://www.virustotal.com/gui/file/94cae63dcbabb71c5dd43f55fd09caeffdcd7628a02a112fb3cba36698ef72bc
- Sigmas
  - https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_mal_creddumper.yml
- Emulation
  - https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.md#atomic-test-1---gsecdump


# CommandLine
~~~
gsecdump -a
gsecdump -1
gsecdump -s
~~~