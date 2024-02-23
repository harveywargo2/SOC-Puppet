import os
import yaml
import socpuppet.hunterpy.kql_qbuild as kbuild


# Path Variables for Module
esentutl_path = os.path.dirname(os.path.abspath(__file__))
esentutl_kql_path = os.path.join(esentutl_path, 'm365d')
esentutl_sigma_path = os.path.join(esentutl_path, 'sigma')


def esentutl_p1000_copy_sam(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(esentutl_kql_path,
                               'esentutl_p1000_copy_sam.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def esentutl_p1001_copy_ntds(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(esentutl_kql_path,
                               'esentutl_p1001_copy_ntds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output