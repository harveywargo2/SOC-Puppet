import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
comsvcs_path = os.path.dirname(os.path.abspath(__file__))
comsvcs_kql_path = os.path.join(comsvcs_path, 'kql')
comsvcs_sigma_path = os.path.join(comsvcs_path, 'sigma')


def comsvcs_p1000_minidump(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1000_minidump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def comsvcs_p1001_rundll32(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1001_rundll32.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def comsvcs_p1002_create_file(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(comsvcs_kql_path,
                               'comsvcs_p1002_create_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output