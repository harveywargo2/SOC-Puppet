import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
comsvcs_path = os.path.dirname(os.path.abspath(__file__))
comsvcs_kql_path = os.path.join(comsvcs_path, 'm365d')
comsvcs_sigma_path = os.path.join(comsvcs_path, 'sigma')


def comsvcs_p1000_created_minidump(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1000_created_minidump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def comsvcs_p1001_minidump_writedump_function_call(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1001_minidump_writedump_function_call.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def comsvcs_p1002_created_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1002_created_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output