# MSHTA - Microsoft HTML Application

## Reference Links
- LOLBAS
  - https://lolbas-project.github.io/lolbas/Binaries/Mshta/
- Mitre Attack
  - https://attack.mitre.org/techniques/T1218/005/
- HTA 
  - https://en.wikipedia.org/wiki/HTML_Application
  - http://blog.sevagas.com/?Hacking-around-HTA-files
  - https://docs.microsoft.com/en-us/dotnet/standard/data/xml/xslt-stylesheet-scripting-using-msxsl-script
- Write Ups
  - https://redcanary.com/threat-detection-report/techniques/mshta/#:~:text=Mshta.exe%20is%20a%20Windows,a%20network%20proxy%2Daware%20fashion.
  - https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
  - https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
  - https://www.trendmicro.com/en_us/research/22/e/avoslocker-ransomware-variant-abuses-driver-file-to-disable-anti-Virus-scans-log4shell.html
  - https://codewhitesec.blogspot.com/2018/07/lethalhta.html
  - https://github.com/codewhitesec/LethalHTA/tree/master/CobaltStrike
  - https://web.archive.org/web/20220830122045/http://blog.talosintelligence.com/2022/08/modernloader-delivers-multiple-stealers.html
  - https://blog.talosintelligence.com/modernloader-delivers-multiple-stealers-cryptominers-and-rats/
  - https://www.trustedsec.com/july-2015/malicious-htas/
  - https://0x00sec.org/t/clientside-exploitation-in-2018-how-pentesting-has-changed/7356
  - https://medium.com/tsscyber/pentesting-and-hta-bypassing-powershell-constrained-language-mode-53a42856c997
- Open Source Detections
  - https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_http.yml
  - https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
  - https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
  - https://eqllib.readthedocs.io/en/latest/analytics/6bc283c4-21f2-4aed-a05c-a9a3ffa95dd4.html
  - https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
  - https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_mshta_susp_child_processes.yml
  - https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
  - https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
  - https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_execution.yml