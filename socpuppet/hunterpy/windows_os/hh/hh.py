import os
import yaml
import socpuppet.hunterpy.kql_qbuild as kbuild


# Path Variables for Module
hh_path = os.path.dirname(os.path.abspath(__file__))
hh_kql_path = os.path.join(hh_path, 'm365d')
hh_sigma_path = os.path.join(hh_path, 'sigma')


def hh_p1000_executing_ps1(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(hh_kql_path,
                               'hh_p1000_executing_ps1.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def hh_p1001_executing_chm(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(hh_kql_path,
                               'hh_p1001_executing_chm.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

