# UAC 


## Ref Links
- Audit User Account Management
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-user-account-management
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4738
  - https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/b10cfda1-f24f-441b-8f43-80cb93e786ec
  - https://learn.microsoft.com/en-US/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties
- https://blog.menasec.net/2019/02/threat-hunting-26-persistent-password.html
- https://vdoc.pub/documents/windows-security-monitoring-scenarios-and-patterns-6k5pema91320
- https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties
- https://www.reddit.com/r/sysadmin/comments/f67o6o/windows_event_id_4738/



| Index   | HEX   | DEC   | Const Enabled   | Const Disabled   | Meaning               |
|---------|-------|-------|-----------------|------------------|-----------------------|
| 0       | 0x01  | 1     | 2080            | 2048             | Account Disabled      |
| 2       | 0x04  | 4     | 2082            | 2050             | Password Not Required |
| 4       | 0x10  | 16    | 2084            | 2052             | Normal Account        | 
| 9       | 0x200 | 512   | 2089            | 2057             | Don't Expire Password | 