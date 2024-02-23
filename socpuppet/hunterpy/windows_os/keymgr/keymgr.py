import os
import yaml
import socpuppet.hunterpy.kql_qbuild as kbuild


# Path Variables for Module
keymgr_path = os.path.dirname(os.path.abspath(__file__))
keymgr_kql_path = os.path.join(keymgr_path, 'm365d')
keymgr_sigma_path = os.path.join(keymgr_path, 'sigma')


def keymgr_p1000_dump_creds(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(keymgr_kql_path,
                               'keymgr_p1000_dump_creds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output
