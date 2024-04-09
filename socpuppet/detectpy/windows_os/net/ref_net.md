# Net Command Line Utility in Windows


## Reference Links
- Mitre Attack
  - https://attack.mitre.org/software/S0039/
- MSFT Doc
  - https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/net-commands-on-operating-systems
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490717(v=technet.10)?redirectedfrom=MSDN
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490718(v=technet.10)
- Threat Intel 
  - https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a
  - https://github.com/DISREL/Conti-Leaked-Playbook-TTPs/blob/main/Conti-Leaked-Playbook-TTPs.pdf


## Net Command Break Out
`net view /all /domain` 
- command in Windows combines two functions to provide a comprehensive overview of shared resources within a specified domain:

`net view`
- This base command lists shared resources and computers on the network.
- This command will only show a list of computers available on your domain or workgroup that have file and printer sharing enabled
- It hides less visible resources.

`net view /all`
- Switches output to include
- All shared resources: This includes hidden administrative shares like C$, D$, IPC$, etc., which are usually hidden for security reasons.
- Hidden resources: These are resources that are shared but not advertised for browsing.
- Offline client caching settings: This shows how remote computers can access the shared resources while offline.

`net group /domain`
`net group /dom`
- This switch focuses the command's output on a particular domain.
- /dom works like /domain

`net view /all /domain`
- Targets a Specific Domain: 
- It directs the command to gather information from the specified domain, rather than your current domain or workgroup.
- Lists All Shared Resources: It displays a list of all shared resources within that domain, including:
  - Regular shared folders and printers
  - Hidden administrative shares
  - Resources not advertised for browsing
  - Includes Offline Caching Settings: It reveals how remote computers can access these shared resources while offline. 

