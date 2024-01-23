import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
mod_path = os.path.dirname(os.path.abspath(__file__))
kql_path = os.path.join(mod_path, 'kql')
sigma_path = os.path.join(mod_path, 'sigma')


def net_p001_cmd_to_list_domain_groups(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p001_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p002_cmd_to_list_users_in_domain_admin_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p002_group_domainadmin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p003_cmd_to_list_users_in_enterprise_admin_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p003_group_enterpriseadmin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p004_cmd_to_list_users_in_domain_users_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p004_group_domainusers.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p005_cmd_to_list_users_in_domain_computers_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p005_group_domaincomputers.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p006_cmd_to_list_users_in_domain_guests_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p006_group_domainguests.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p007_cmd_to_list_users_in_keyword_admin_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p007_group_keyword_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p008_cmd_to_list_users_in_monitored_keyword_group(*, type='kql', kql_ago='1d'):
    word_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p008_group_keyword_match.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_var_query_builder(data, kql_ago)

    else:
        output = f'type={type} not supported'

    return output


def net_p100_cmd_to_list_local_groups(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p100_localgroup.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p101_cmd_to_add_user_to_local_group(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p101_localgroup_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p102_cmd_to_list_user_in_local_group_administrators(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p102_localgroup_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p103_cmd_to_add_user_to_local_group_administrators(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p103_localgroup_admin_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p104_cmd_to_list_user_in_local_group_rdp(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p104_localgroup_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p105_cmd_to_add_user_in_local_group_rdp(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p105_localgroup_rdp_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output

