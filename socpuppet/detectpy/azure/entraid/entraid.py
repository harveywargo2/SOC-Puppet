import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
entra_path = os.path.dirname(os.path.abspath(__file__))
entra_kql_path = os.path.join(entra_path, 'kql')
entra_sigma_path = os.path.join(entra_path, 'sigma')


def entraid_p1000_role_mgt_global_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1000_role_mgt_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output