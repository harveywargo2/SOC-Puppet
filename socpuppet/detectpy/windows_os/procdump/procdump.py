import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
procd_path = os.path.dirname(os.path.abspath(__file__))
procd_kql_path = os.path.join(procd_path, 'm365d')
procd_sigma_path = os.path.join(procd_path, 'sigma')


def procdump_p1000_lsass_cmd(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(procd_kql_path,
                               'procdump_p1000_lsass_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def procdump_p1001_dumping_process(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(procd_kql_path,
                               'procdump_p1001_dumping_process.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def procdump_p1002_renamed(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(procd_kql_path,
                               'procdump_p1002_renamed.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output
