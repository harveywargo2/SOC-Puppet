import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
wuauclt_path = os.path.dirname(os.path.abspath(__file__))
wuauclt_kql_path = os.path.join(wuauclt_path, 'kql_m365d')
wuauclt_sigma_path = os.path.join(wuauclt_path, 'sigma')


def wuauclt_p1000_execute_dll(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(wuauclt_kql_path,
                               'wuauclt_p1000_execute_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output