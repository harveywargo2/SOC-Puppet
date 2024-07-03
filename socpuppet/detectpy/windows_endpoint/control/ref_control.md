# Control.exe

## Reference Links
- LOLBAS 
  - https://lolbas-project.github.io/lolbas/Binaries/Control/
- MSFT Docs
  - https://docs.microsoft.com/en-us/windows/desktop/shell/executing-control-panel-items
- Write Up
  - https://pentestlab.blog/2017/05/24/applocker-bypass-control-panel/
  - https://www.contextis.com/resources/blog/applocker-bypass-registry-key-manipulation/
  - https://bohops.com/2018/01/23/loading-alternate-data-stream-ads-dll-cpl-binaries-to-bypass-applocker/
- Open Source Detections
  - https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
  - https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
  - https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
  - https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml