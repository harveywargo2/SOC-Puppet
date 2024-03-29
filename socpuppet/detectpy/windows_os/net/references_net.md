# Net Command Line Utility in Windows

Net Command Line Utility is commonly used by Cyber Threat Actors to 
- Perform AD Enumeration 
- Discovery of Users Information 
- Discovery of System Information 
- Discovery of Password Policy 
- Modify Local Groups & Users 
- Discovery Network Shares


## Reference Links
- Mitre: https://attack.mitre.org/software/S0039/)
- https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/net-commands-on-operating-systems
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490717(v=technet.10)?redirectedfrom=MSDN
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490718(v=technet.10)
- TI: https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/
- TI: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a
- TI: https://github.com/DISREL/Conti-Leaked-Playbook-TTPs/blob/main/Conti-Leaked-Playbook-TTPs.pdf


## Net Command Break Out 

The `net view /all /domain` 
command in Windows combines two functions to provide a comprehensive overview of shared resources within a specified domain:

Here's a breakdown of its components:

`net view`: As you know, this base command lists shared resources and computers on the network.
By itself, this command will only show a list of computers available on your domain or workgroup that have file and printer sharing enabled. It hides less visible resources.

`/all`: Switches output to include
- All shared resources: This includes hidden administrative shares like C$, D$, IPC$, etc., which are usually hidden for security reasons.
- Hidden resources: These are resources that are shared but not advertised for browsing.
- Offline client caching settings: This shows how remote computers can access the shared resources while offline.

`/domain`: This switch focuses the command's output on a particular domain.

When combined, `net view /all /domain` performs these actions:

Targets a Specific Domain: It directs the command to gather information from the specified domain, rather than your current domain or workgroup.

Lists All Shared Resources: It displays a list of all shared resources within that domain, including:
- Regular shared folders and printers
- Hidden administrative shares
- Resources not advertised for browsing
- Includes Offline Caching Settings: It reveals how remote computers can access these shared resources while offline. 

Excludes External Domains: It restricts the output to the specified domain, omitting resources from other domains on the network.

In essence, this command provides a thorough view of all shared resources within a designated domain, including those that are typically hidden.
It's useful for:
- Network administrators to manage and monitor shared resources within their domain.
- Troubleshooting network connectivity issues related to shared resources.
- Security professionals to identify potential vulnerabilities or unauthorized shares.

Here are some additional things to keep in mind:

The `net view /all` command relies on NetBIOS for communication. 
- If NetBIOS is disabled on your network or the target computer, you might not get accurate results.
- Running this command might generate some network traffic, especially if you're targeting a large number of computers.
- Some older versions of Windows might not support the /all switch.

