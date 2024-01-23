import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
mod_path = os.path.dirname(os.path.abspath(__file__))
kql_path = os.path.join(mod_path, 'kql')
sigma_path = os.path.join(mod_path, 'sigma')


def net_p1000_cmd_used_to_list_groups_on_domain(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1000_cmd_used_to_list_groups_on_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)

    else:
        output = f'type={type} not supported'

    return output


def net_p1001_cmd_used_to_list_users_in_domain_admins_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1001_cmd_used_to_list_users_in_domain_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1002_cmd_used_to_list_users_in_enterprise_admins_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1002_cmd_used_to_list_users_in_enterprise_admins_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1003_cmd_to_list_users_in_domain_users_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1003_cmd_used_to_list_users_in_domain_users_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1004_cmd_used_to_list_users_in_domain_computers_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1004_cmd_used_to_list_users_in_domain_computers_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1005_cmd_to_list_users_in_domain_guests_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1005_cmd_used_to_list_users_domain_guests_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1006_cmd_used_to_list_users_keyword_admin_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1006_cmd_used_to_list_users_keyword_admin_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p1007_cmd_used_to_list_users_in_monitored_list_match(*, type='kql', kql_ago='1d'):
    word_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p1007_cmd_used_to_list_users_in_monitored_list_match.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)

    else:
        output = f'type={type} not supported'

    return output


def net_p2000_cmd_used_to_list_local_groups(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2000_cmd_used_to_list_local_groups.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p2001_cmd_used_to_add_user_to_local_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2001_cmd_used_to_add_user_to_local_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p2002_cmd_used_to_list_users_in_local_group_administrators(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2002_cmd_used_to_list_users_in_local_group_administrators.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p2003_cmd_used_to_list_users_in_local_group_rdp(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2003_cmd_used_to_list_users_in_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p2004_cmd_used_to_add_user_to_local_group_administrators(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2004_cmd_used_to_add_user_to_local_group_administrators.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p2005_cmd_used_to_add_user_to_local_group_rdp(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p2005_cmd_used_to_add_user_to_local_group_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output

