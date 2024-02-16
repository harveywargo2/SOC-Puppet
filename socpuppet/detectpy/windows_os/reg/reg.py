import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
reg_path = os.path.dirname(os.path.abspath(__file__))
reg_kql_path = os.path.join(reg_path, 'm365d')
reg_sigma_path = os.path.join(reg_path, 'sigma')


def reg_p1000_hklm_sam_dump(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(reg_kql_path,
                               'reg_p1000_hklm_sam_dump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def reg_p10001_hklm_lsa_dump(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(reg_kql_path,
                               'reg_p1001_hklm_lsa_dump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output