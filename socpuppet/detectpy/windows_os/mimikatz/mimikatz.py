import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mimikatz_path = os.path.dirname(os.path.abspath(__file__))
mimikatz_kql_path = os.path.join(mimikatz_path, 'm365d')
mimikatz_sigma_path = os.path.join(mimikatz_path, 'sigma')


def mimikatz_p0001_file_indicator(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p0001_file_indicator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p0002_file_indicator(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p0002_file_indicator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1000_cmd_sekurlsa(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1000_cmd_sekurlsa.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1001_cmd_lsadump(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1001_cmd_lsadump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1002_cmd_kerberos(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1002_cmd_kerberos.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1003_cmd_crypto(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1003_cmd_crypto.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1004_cmd_vault(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1004_cmd_vault.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1005_cmd_dpapi(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1005_cmd_dpapi.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1006_cmd_event(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1006_cmd_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1007_cmd_misc(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1007_cmd_misc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1008_cmd_privilege(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1008_cmd_privilege.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1009_cmd_process(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1009_cmd_process.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def mimikatz_p1010_cmd_rpc(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(mimikatz_kql_path,
                               'mimikatz_p1010_cmd_rpc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

