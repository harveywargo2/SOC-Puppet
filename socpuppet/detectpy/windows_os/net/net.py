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


def net_p0002_potential_dump_to_file(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p0002_potential_dump_to_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1000_cmd_used_to_list_groups_on_domain(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path, 'net_p1000_cmd_used_to_list_groups_on_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')

    else:
        output = f'type={type} not supported'

    return output


def net_p1001_cmd_used_to_list_users_in_domain_admins_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1001_cmd_used_to_list_users_in_domain_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1002_cmd_used_to_list_users_in_enterprise_admins_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1002_cmd_used_to_list_users_in_enterprise_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1003_cmd_to_list_users_in_domain_users_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1003_cmd_used_to_list_users_in_domain_users_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1004_cmd_used_to_list_users_in_domain_computers_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1004_cmd_used_to_list_users_in_domain_computers_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1005_cmd_to_list_users_in_domain_guests_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1005_cmd_used_to_list_users_domain_guests_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1006_cmd_used_to_list_users_keyword_admin_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1006_cmd_used_to_list_users_keyword_admin_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p1007_cmd_used_to_list_users_in_monitored_list_match(*, type='m365d', kql_ago='1d'):
    word_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p1007_cmd_used_to_list_users_in_monitored_list_match.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')

    else:
        output = f'type={type} not supported'

    return output


def net_p2000_cmd_used_to_list_local_groups(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2000_cmd_used_to_list_local_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2001_cmd_used_to_add_user_to_local_group(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2001_cmd_used_to_add_user_to_local_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2002_cmd_used_to_list_users_in_local_group_administrators(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2002_cmd_used_to_list_users_in_local_group_administrators.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2003_cmd_used_to_list_users_in_local_group_rdp(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2003_cmd_used_to_list_users_in_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2004_cmd_used_to_add_user_to_local_group_administrators(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2004_cmd_used_to_add_user_to_local_group_administrators.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p2005_cmd_used_to_add_user_to_local_group_rdp(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p2005_cmd_used_to_add_user_to_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3000_cmd_used_to_list_users_on_device(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3000_cmd_used_to_list_users_on_device.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3001_cmd_used_to_list_users_on_domain(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3001_cmd_used_to_list_users_on_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3002_cmd_used_to_list_details_of_admin_user(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3002_cmd_used_to_list_details_of_admin_user.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3003_cmd_used_to_add_user_to_device(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3003_cmd_used_to_add_user_to_device.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p3004_cmd_used_to_add_user_to_domain(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p3004_cmd_used_to_add_user_to_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4000_cmd_used_to_view_all_shared_resources(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4000_cmd_used_to_view_all_shared_resources.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4001_cmd_used_to_view_file_print_share_devices(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4001_cmd_used_to_view_file_print_share_devices.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p4002_cmd_used_to_view_all_shared_resources_domain(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p4002_cmd_used_to_view_all_shared_resources_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p5000_cmd_used_to_stop_service(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p5000_cmd_used_to_stop_service.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def net_p5001_cmd_used_to_stop_defender_service(*, type='m365d', kql_ago='1d'):

    if type == 'm365d':
        with open(os.path.join(net_kql_path,
                               'net_p5001_cmd_used_to_stop_defender_service.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

