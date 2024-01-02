

def net_group_cmd_run(x='1d'):
    detect = {
        'title': 'Net Group Command Run',
        'detectCon': 'SinglePatternMatch-5',
        'attackTechniqueId': 'T1069.001',
        'attackSoftwareId': 'S0039',
        'detectionUseCase': '',
        'dataFlow': 'MsftDefenderEndpoint (ON) WindowsOS [LOGS] ProcessCreation {FWDS} DeviceProcessEvents',
        'codeBase': 'kql',
        'query': f'''
            DeviceProcessEvents
            | where Timestamp >= ago({x})
            | where FileName has_any ('net', 'net1', 'cmd', 'powershell') 
                and ProcessCommandLine has 'net'
                and ProcessCommandLine has_any ('group', 'groups')
            '''
    }
    return detect

