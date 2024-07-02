# NLTEST - Network Location Test

## Reference Links
- Attack Software
  - https://attack.mitre.org/software/S0359/
- MSFT Doc
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731935(v=ws.11)
- Command Doc
  - https://ss64.com/nt/nltest.html
- Intel
  - https://redcanary.com/threat-detection-report/techniques/domain-trust-discovery/
  - https://harmj0y.medium.com/a-guide-to-attacking-domain-trusts-ef5f8992bb9d

## Notable Commands  
- `nltest` 
  - A Windows command-line utility for managing and troubleshooting network logins and domain trusts.
- `/dclist`
  - list all DCs 
- /trusted_domains
  - determines if a NetLogon Session can be established
- `/dsgetdc`
  - query DNS for list of DCs and IP Addresses
- `/domain_trusts` 
  - This switch instructs the command to list trusted domains.
- `/all_trusts`
  - This switch specifies that the command should display all trusted domains, including:
    - Domains explicitly trusted by the current domain
    - Domains that explicitly trust the current domain
    - Domains in the same forest as the current domain