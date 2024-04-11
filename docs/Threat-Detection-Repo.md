## Detection Logic Repos
- https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules
- https://github.com/Azure/Azure-Sentinel
- https://github.com/reprise99/Sentinel-Queries
- https://github.com/SigmaHQ/sigma
- https://github.com/splunk/security_content
- https://github.com/chronicle/detection-rules
- https://github.com/bfuzzy/auditd-attack
- https://github.com/mbabinski/Sigma-Rules
- https://github.com/elastic/detection-rules
- https://github.com/The-DFIR-Report/Sigma-Rules/tree/main/rules

# SIGMA
- Generic and open signature format that allows you to describe relevant log events
- Standard repo for open source detections
- Yara for logs stored in yaml
- https://github.com/SigmaHQ/sigma
- https://github.com/SigmaHQ/sigma-specification/blob/main/Tags_specification.md
- https://github.com/SigmaHQ/sigma-specification/blob/main/Taxonomy_specification.md
- https://socprime.com/blog/sigma-rules-the-beginners-guide/

### Rule Yaml
~~~
title:
id:
status:
description:
author:
references:
tags:
logsource: 
    category:
    product:
detection:
    selection:
    filter:
    condition:
falsepositives:
level:
~~~

### Minimum Fields
~~~
title: sigma title
description:
references:
    - 
logsource:
    category: 
    product: 
detection:
    selection:
    condition: selection
~~~