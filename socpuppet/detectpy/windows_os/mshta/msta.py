import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mshta_path = os.path.dirname(os.path.abspath(__file__))
mshta_kql_path = os.path.join(mshta_path, 'kql')
mshta_sigma_path = os.path.join(mshta_path, 'sigma')


def mshta_p1000_executing_vbs(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mshta_kql_path,
                               'netsh_p0001_disable_windows_firewall.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output

