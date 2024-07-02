# Netsh - Network Shell


## Reference Links
- MSFT Command Doc
  - https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-contexts
  - https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh
  - https://ss64.com/nt/netsh.html
- Intel & POC Write Ups
  - https://labs.sentinelone.com/sarwent-malware-updates-command-detonation/
  - https://app.any.run/tasks/210244b9-0b6b-4a2c-83a3-04bd3175d017/
  - https://www.winhelponline.com/blog/enable-and-disable-windows-firewall-quickly-using-command-line/
- NetSh helper Beacon
  - https://web.archive.org/web/20160928212230/https://www.adaptforward.com/2016/09/using-netshell-to-execute-evil-dlls-and-persist-on-a-host/
  - https://github.com/outflanknl/NetshHelperBeacon
- Port Forwarding Port Proxy
  - https://www.dfirnotes.net/portproxy_detection/
  - https://adepts.of0x.cc/netsh-portproxy-code/
  - https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html


The command `netsh firewall set service type =remotedesktop mode = enable` 
- enables the Remote Desktop feature on your Windows machine in a slightly different way than the previous one. 
- `netsh firewall`
  - This refers to the Network Shell utility for managing firewall settings.
- `set service`
  - This command focuses on configuring settings for specific services.
- `type = remotedesktop`
  - This specifies the service you want to modify, which is Remote Desktop in this case.
- `mode = enable`
  - This activates the Remote Desktop service within the firewall.
- This command directly targets the service itself, while the previous one focused on a specific rule group.



Default Rule Groups: These groups are present across most Windows editions:
- Remote Desktop: Manages rules related to Remote Desktop connections. 
- Remote Assistance: Controls rules for remote assistance features. 
- Windows Remote Management (WinRM): Governs rules for the WinRM service used for remote management. 
- Shared Folder Discovery: Enables or disables discovery of shared folders on the network. 
- HomeGroup Network Discovery: Controls discovery of HomeGroup networks. 
- File and Printer Sharing: Manages rules for file and printer sharing services. 
- Windows Media Center Service: Governs rules for the Windows Media Center service. 
- Network Discovery: Enables or disables network discovery for different network locations. 
- Inbound Rules: Catches all inbound rules not assigned to other specific groups. 
- Outbound Rules: Catches all outbound rules not assigned to other specific groups.


Additional Rule Groups: These groups might be present depending on your Windows edition and version:
- BITS: Manages rules for the Background Intelligent Transfer Service (BITS). 
- Guest: Controls rules for the Guest account access. 
- Hyper-V: Governs rules for Hyper-V virtualization features. 
- Internet Explorer (Protected Mode): Manages rules for Internet Explorer in Protected Mode. 
- Loopback: Controls rules for the loopback adapter. 
- Media Streaming: Governs rules for media streaming services. 
- Remote Access: Handles rules for remote access connections. 
- RPC: Manages rules for Remote Procedure Call (RPC) services. 
- SNMP Trap: Controls rules for receiving SNMP traps. 
- SQL Server: Governs rules for the SQL Server service. 
- WebDAV: Manages rules for the Web Distributed Authoring and Versioning (WebDAV) service. 
- Windows Defender Firewall: Present in Windows 10 and later, it contains built-in firewall rules managed by Windows Defender.