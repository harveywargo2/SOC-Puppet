# SIGMA
- Generic and open signature format that allows you to describe relevant log events
- Standard repo for open source detections
- Yara for logs stored in yaml

## Ref Links
- https://github.com/SigmaHQ/sigma-specification/blob/main/Tags_specification.md
- https://github.com/SigmaHQ/sigma-specification/blob/main/Taxonomy_specification.md
- https://socprime.com/blog/sigma-rules-the-beginners-guide/
- https://docs.blusapphire.io/sigma-rules/understanding-sigma-rule

## Rule Yaml
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

## Minimum Fields
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

