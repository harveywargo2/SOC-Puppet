import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mde_path = os.path.dirname(os.path.abspath(__file__))
mde_kql_path = os.path.join(mde_path, 'kql_m365d')
mde_sigma_path = os.path.join(mde_path, 'sigma')


def mdebuiltin_p1000_t1003_tag(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mde_kql_path,
                               'mdebuiltin_p1000_t1003_tag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mdebuiltin_p2000_msdt_follina(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mde_kql_path,
                               'mdebuiltin_p2000_msdt_follina.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

