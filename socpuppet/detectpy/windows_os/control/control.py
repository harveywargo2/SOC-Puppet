import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
control_path = os.path.dirname(os.path.abspath(__file__))
control_kql_path = os.path.join(control_path, 'm365d')
control_sigma_path = os.path.join(control_path, 'sigma')


def control_p1000_executing_cpl_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(control_kql_path,
                               'control_p1000_executing_cpl_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def control_p1001_executing_dll_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(control_kql_path,
                               'control_p1001_executing_dll_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

