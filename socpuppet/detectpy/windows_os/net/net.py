import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
mod_path = os.path.dirname(os.path.abspath(__file__))
kql_path = os.path.join(mod_path, 'kql')
sigma_path = os.path.join(mod_path, 'sigma')


def net_group_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_group_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'


    return output

