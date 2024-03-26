import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
net_path = os.path.dirname(os.path.abspath(__file__))
net_kql_path = os.path.join(net_path, 'm365d')
net_sigma_path = os.path.join(net_path, 'sigma')


def net_p0001_cmd_used_and_piped_to_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p0001_cmd_used_and_piped_to_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p0002_created_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p0002_created_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p0003_file_signer_name_mismatch(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p0003_file_signer_name_mismatch.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1000_list_domain_groups(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p1000_list_domain_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')

    else:
        output = f'type={type} not supported'

    return output


def net_p1001_add_user_domain_group(*, type='m365d', kql_ago='1d'):
    word_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1001_add_user_domain_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')

    else:
        output = f'type={type} not supported'

    return output


def net_p1002_list_domain_admins_group_users(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1002_list_domain_admins_group_users.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1003_add_user_domain_admins_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1003_add_user_domain_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1004_list_enterprise_admins_group_users(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1004_list_enterprise_admins_group_users.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1005_add_user_enterprise_admins_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1005_add_user_enterprise_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1006_list_admins_group_users(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1006_list_admins_group_users.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1007_list_users_in_monitored_list_match(*, type='m365d', kql_ago='1d'):
    word_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1007_list_users_in_monitored_list_match.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')

    else:
        output = f'type={type} not supported'

    return output


def net_p2000_list_local_groups(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2000_list_local_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2001_add_user_to_local_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2001_add_user_to_local_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2002_list_users_local_group_admins(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2002_list_users_local_group_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2003_list_users_in_local_group_rdp(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2003_list_users_in_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2004_add_user_to_local_group_admins(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2004_add_user_to_local_group_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2005_add_user_to_local_group_rdp(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2005_add_user_to_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3000_list_users_on_device(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3000_list_users_on_device.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3001_list_domain_users(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3001_list_domain_users.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3002_list_details_of_admin_user(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3002_list_details_of_admin_user.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4000_view_visible_computers(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4000_view_visible_computers.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4001_view_visible_computers_hidden_shares(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4001_view_visible_computers_hidden_shares.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4002_stop_defender_service(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4002_stop_defender_service.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

