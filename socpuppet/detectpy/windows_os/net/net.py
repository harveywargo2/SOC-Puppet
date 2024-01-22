import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
mod_path = os.path.dirname(os.path.abspath(__file__))
kql_path = os.path.join(mod_path, 'kql')
sigma_path = os.path.join(mod_path, 'sigma')


def net_p001_group_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p001_group_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p002_group_domain_admin_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p002_group_domain_admin_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p003_group_enterprise_admin_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p003_group_enterprise_admin_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p004_group_domain_users_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p004_group_domain_users_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p005_group_domain_computers_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p005_group_domain_computers_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p006_group_domain_guests_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p006_group_domain_guests_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p007_group_keyword_admin_cmd(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p007_group_keyword_admin_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_query_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def net_p008_group_keyword_list_match_cmd(*, type='kql', kql_ago='1d'):
    mon_list = "let KeywordList = dynamic(['server', 'service accounts', 'linux server', 'linux']);"


    if type == 'kql':
        with open(os.path.join(kql_path, 'net_p008_group_keyword_match_cmd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        logic = mon_list + data.get('kqlTable') + f' | where Timestamp >= ago({kql_ago})' + data.get('kqlQuery')
        output = {'query': logic}

    else:
        output = f'type={type} not supported'

    return output

