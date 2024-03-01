import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mimikatz_path = os.path.dirname(os.path.abspath(__file__))
mimikatz_kql_path = os.path.join(mimikatz_path, 'm365d')
mimikatz_sigma_path = os.path.join(mimikatz_path, 'sigma')


def mimikatz_p0001_file_a(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p0001_file_a.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p0002_file_b(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p0002_file_b.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1000_cmds(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1000_cmds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


