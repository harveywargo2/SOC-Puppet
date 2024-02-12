import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mshta_path = os.path.dirname(os.path.abspath(__file__))
mshta_kql_path = os.path.join(mshta_path, 'kql')
mshta_sigma_path = os.path.join(mshta_path, 'sigma')


def mshta_p1000_executing_hta(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mshta_kql_path,
                               'mshta_p1000_executing_hta.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mshta_p1001_executing_vbs(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mshta_kql_path,
                               'mshta_p1001_executing_vbs.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mshta_p1002_executing_javascript(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mshta_kql_path,
                               'mshta_p1002_executing_javascript.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output