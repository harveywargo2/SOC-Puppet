
## DFIR (CommandLine-Detect-Samples-IOC)
- https://thedfirreport.com/2022/04/04/stolen-images-campaign-ends-in-conti-ransomware/
- https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/
- https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/
- https://thedfirreport.com/2020/10/08/ryuks-return/#:~:text=The%20Ryuk%20group%20went%20from,Rubeus%20to%20accomplish%20their%20objective.
- https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/


SIGMA
- https://github.com/SigmaHQ/sigma/blob/a3eed2b760abddfd62014fcf9ae81f435b216473/rules/windows/process_access/proc_access_win_lsass_memdump.yml
- https://github.com/SigmaHQ/sigma/blob/11b6b24660c045bb907ed43cfe007349764173bc/rules/windows/powershell/powershell_script/posh_ps_powerview_malicious_commandlets.yml
- https://github.com/SigmaHQ/sigma/blob/071bcc292362fd3754a2da00878bba4bae1a335f/rules/windows/process_creation/proc_creation_win_ad_find_discovery.yml
- https://github.com/SigmaHQ/sigma/blob/6b3fc11a48e8aa2773dfe266c3be11e4c4c973a5/rules/windows/process_creation/proc_creation_win_powershell_defender_disable_feature.yml
- https://github.com/SigmaHQ/sigma/blob/eb382c4a59b6d87e186ee269805fe2db2acf250e/rules/windows/builtin/security/win_admin_share_access.yml
- https://github.com/SigmaHQ/sigma/blob/04f72b9e78f196544f8f1331b4d9158df34d7ecf/rules/windows/builtin/application/win_software_atera_rmm_agent_install.yml
- https://github.com/SigmaHQ/sigma/blob/8bb3379b6807610d61d29db1d76f5af4840b8208/rules/windows/process_creation/proc_creation_win_trust_discovery.yml
- https://github.com/SigmaHQ/sigma/blob/becf3baeb4f6313bf267f7e8d6e9808fc0fc059c/rules/windows/process_creation/proc_creation_win_susp_recon_activity.yml
- https://github.com/SigmaHQ/sigma/blob/e049058d14dd9ec09771b38ed4d59e8b49ba1bad/rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/malware/win_mal_ryuk.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_powershell_suspicious_parameter_variation.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_trust_discovery.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_net_execution.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_powershell_suspicious_parameter_variation.yml
- https://github.com/Neo23x0/sigma/blob/82cae6d63c9c2f6d3e86c57e11497d86279b9f95/rules/windows/process_creation/win_susp_wmi_execution.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/other/win_defender_disabled.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/malware/win_mal_ryuk.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/powershell/powershell_shellcode_b64.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_shadow_copies_deletion.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_net_execution.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_whoami.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_wmi_execution.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_trust_discovery.yml
- https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_whoami_as_system.yml
- rclone_execution.yaml 
- sysmon_in_memory_powershell.yml 
- win_susp_wmic_proc_create_rundll32.yml 
- sysmon_abusing_debug_privilege.yml 
- win_trust_discovery.yml 
- win_office_shell.yml 
- win_mshta_spawn_shell.yml 
- win_susp_net_execution.yml 
- win_susp_regsvr32_anomalies.yml 
- sysmon_rundll32_net_connections.yml 
- win_net_enum.yml 
- win_susp_wmi_execution.yml

Tools 
- SplashTop
- AnyDesk
- ProcessHacker

## Github Playbook Leak (CommandLine)
- https://github.com/DISREL/Conti-Leaked-Playbook-TTPs/blob/main/Conti-Leaked-Playbook-TTPs.pdf

Tools
- NGROK
- ADFind
- PowerSploit
- Atera Agent

## Talos
- https://blog.talosintelligence.com/conti-leak-translation/)

## BleepingComputer (Tools)
- https://www.bleepingcomputer.com/news/security/translated-conti-ransomware-playbook-gives-insight-into-attacks/

Tools
- Armitage
- SharpView
- SharpChrome
- SeatBelt
- ADFind
- GMER
- SMBAutoBrute
- Kerberoasting
- Mimikatz
- RouterScan
- AnyDesk
- Atera