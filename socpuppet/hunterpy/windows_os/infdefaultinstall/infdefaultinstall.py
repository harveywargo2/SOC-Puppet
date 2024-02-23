import os
import yaml
import socpuppet.hunterpy.kql_qbuild as kbuild


# Path Variables for Module
infd_path = os.path.dirname(os.path.abspath(__file__))
infd_kql_path = os.path.join(infd_path, 'm365d')
infd_sigma_path = os.path.join(infd_path, 'sigma')


def infdefaultinstall_p1000_executing_inf(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(infd_kql_path,
                               'infdefaultinstall_p1000_executing_inf.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output