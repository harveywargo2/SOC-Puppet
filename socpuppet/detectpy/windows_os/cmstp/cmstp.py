import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
cmstp_path = os.path.dirname(os.path.abspath(__file__))
cmstp_kql_path = os.path.join(cmstp_path, 'm365d')
cmstp_sigma_path = os.path.join(cmstp_path, 'sigma')


def cmstp_p1000_executing_inf_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1000_executing_inf_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def cmstp_p1001_executing_inf_file_silent_flag(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1001_executing_inf_file_silent_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def cmstp_p1002_executing_inf_file_all_profiles(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1002_executing_inf_all_profiles_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def cmstp_p1003_executing_inf_file_single_user(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1003_executing_inf_single_user_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def cmstp_p1004_spawning_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1003_spawning_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

