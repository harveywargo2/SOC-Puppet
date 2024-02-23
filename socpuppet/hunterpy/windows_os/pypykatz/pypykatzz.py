import os
import yaml
import socpuppet.hunterpy.kql_qbuild as kbuild


# Path Variables for Module
pykz_path = os.path.dirname(os.path.abspath(__file__))
pykz_kql_path = os.path.join(pykz_path, 'm365d')
pykz_sigma_path = os.path.join(pykz_path, 'sigma')


def pypykatz_p1000_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(pykz_kql_path,
                               'pypykatz_p1000_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def pypykatz_p1001_lsass_cmds(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(pykz_kql_path,
                               'pypykatz_p1001_lsass_cmds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

