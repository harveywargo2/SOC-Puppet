# appcmd

## References
- MSFT Docs
  - https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe
- Commands
  - https://medium.com/@anuketjain007/basic-commands-to-manage-website-apppool-in-iis-71366d0accec
  - https://gist.github.com/jetstreamin/c82862e6c4a0e334a2e3
- Sigma
  - https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_service_account_password_dumped.yml
  - 


## Command Info & Flags
list apppool
  - This is the specific command being executed by appcmd.exe. 
  - It tells appcmd to list the application pools.
/@t:*
  - This is an option for the list apppool command. 
  - Here's a breakdown of the option:
/@t 
  - This specifies that we want to view additional information about the application pools beyond their names.
/@t:*" 
  - The asterisk (*) is a wildcard character. 
  - In this context, it means we want to see all available properties (*) for each application pool (@t).
/@text:*: 
  - This option controls the output format.
/@text: 
  - This instructs AppCmd to display the output in plain text format, making it human-readable.
/:*: 
  - This wildcard character (*) tells AppCmd to include all available properties for each application pool in the text output.
/text :* 
  - This is an option for the list apppool command. It controls the output format:
/text 
  - specifies text output (default behavior).
*/text: 
  - instructs AppCmd to display all available properties for each application pool in a detailed format. 
  - This provides comprehensive information about each pool's configuration.


In simpler terms, this command displays a detailed list of all application pools configured on your IIS server. 
The detailed information might include:

Application pool name: 
- The unique identifier assigned to each pool.
Managed by: 
- The identity under which the application pool runs (e.g., Network Service, ApplicationPoolIdentity).
State: 
- Whether the pool is currently started, stopped, or recycling.
Mode: The worker process architecture used by the pool (e.g., 32-bit, 64-bit).
Recycling: Configuration details for application pool recycling, such as frequency or memory limits.
And potentially other properties depending on your IIS configuration.