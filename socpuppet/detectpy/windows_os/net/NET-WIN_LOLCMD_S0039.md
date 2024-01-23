# Net Command Line Utility in Windows

Net Command Line Utility is commonly used by Cyber Threat Actors to 
1. Perform AD Enumeration
2. Discovery of Users Information
3. Discovery of System Information 
4. Discovery of Password Policy
4. Modify Local Groups & Users


## References
- [Mitre Attack Software - S0039](https://attack.mitre.org/software/S0039/)
- https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/net-commands-on-operating-systems
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490717(v=technet.10)?redirectedfrom=MSDN
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490718(v=technet.10)

### Atomic Red 

## Patterns 
#### NET_P001 - Net Group Command
Specific Pattern used to get list of user in the specified group
~~~
net group /domain
net group /dom
~~~

#### NET_P002 - Net Group "Domain Admin" Command
Specific Pattern used to get list of user in the specified group
~~~
net group "domain admins" /domain
~~~

#### NET_P003 - Net Group "Enterprise Admin" Command
Specific Pattern used to get list of user in the specified group
~~~
net group "enterprise admins" /domain
~~~

#### NET_P004 - Net Group "Domain Users" Command 
Specific Pattern used to get list of user in the specified group
~~~
net group "domain users" /domain
net group /domain "domain users"
~~~

#### NET_P005 - Net Group "Domain Computers" Command
Specific Pattern used to get list of user in the specified group
~~~
net group "domain computers" /domain
~~~

#### NET_P006 - Net Group "Domain Guests" Command
Specific Pattern used to get list of user in the specified group
~~~
net group "domain guests" /domain
~~~
#### NET_P007 - Net Group Keyword "Admin" Command
Matches keyword `admin, admins, administrator, administrators` as these may be common naming conventions 
for custom AD Groups

#### NET_P008 - Net Group Keyword From List Match Command

KQL Only 
Sets a variable with a dynamic list.

