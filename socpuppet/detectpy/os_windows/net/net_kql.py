

def net_group_cmd_run(x='1d'):
    logic_json = {
        "type": "Simple_Pattern_Match",
        "title": "Net Group Command Run",
        "detectCon": "5",
        "attackTechniqueId": "T1069.001",
        "attackSoftwareId": "S0039",
        "lolBin": ["net"],
        "dataSource": "Process_Creation",
        "platform": "MSFT_Defender_Endpoint",
        "query": f"""
            DeviceProcessEvents
            | where Timestamp >= ago({x})
            | where FileName has_any ('net', 'net1', 'cmd', 'powershell') 
                and ProcessCommandLine has 'net'
                and ProcessCommandLine has_any ('group', 'groups')
            """,
    }
    return logic_json