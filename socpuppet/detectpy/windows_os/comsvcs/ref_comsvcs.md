# Comsvcs 


## Reference Links
- COMSVCS Funtions
  - https://strontic.github.io/xcyclopedia/library/comsvcs.dll-67B51761A4BC3BD1B5367A22BA1A5B65.html
- LOLBAS
  - https://lolbas-project.github.io/lolbas/Libraries/comsvcs/
- Example Patterns
  - https://gist.github.com/JohnLaTwC/3e7dd4cd8520467df179e93fb44a434e
- Write Up: 
  - https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/
  - https://www.hawk-eye.io/2022/09/tools-used-for-dumping-of-rdpcreds-via-comsvcs-dll/
  - https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz
- LSASSY Dump Method
  - https://github.com/Hackndo/lsassy/blob/14d8f8ae596ecf22b449bfe919829173b8a07635/lsassy/dumpmethod/comsvcs.py
- Open Source Detections
  - https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml
  - https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_access/proc_access_win_lsass_dump_comsvcs_dll.yml
  - https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
  - https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/dump_lsass_via_comsvcs_dll.yml