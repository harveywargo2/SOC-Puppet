import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
entra_path = os.path.dirname(os.path.abspath(__file__))
entra_kql_path = os.path.join(entra_path, 'kql')
entra_sigma_path = os.path.join(entra_path, 'sigma')


def entraid_p1000_role_mgt_global_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1000_role_mgt_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1001_role_mgt_app_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1001_role_mgt_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1002_role_mgt_app_dev(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1002_role_mgt_app_dev.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1003_role_mgt_authentication_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1003_role_mgt_authentication_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1004_role_mgt_auth_policy_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1004_role_mgt_auth_policy_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1005_role_mgt_ief_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1005_role_mgt_ief_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1006_role_mgt_billing_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1006_role_mgt_billing_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1007_role_mgt_cloud_app_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1007_role_mgt_cloud_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1008_role_mgt_cloud_device_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1008_role_mgt_cloud_device_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1009_role_mgt_domain_name_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1008_role_mgt_cloud_device_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1010_role_mgt_directory_sync(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1010_role_mgt_directory_sync.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1011_role_mgt_directory_writer(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1011_role_mgt_directory_writer.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1012_role_mgt_global_reader(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1012_role_mgt_global_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1013_role_mgt_groups_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1013_role_mgt_groups_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1014_role_mgt_helpdesk_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1014_role_mgt_helpdesk_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1015_role_mgt_hybrid_identity_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1015_role_mgt_hybrid_identity_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1016_role_mgt_intune_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1016_role_mgt_intune_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1017_role_mgt_password_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1017_role_mgt_password_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1018_role_mgt_privileged_auth_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1018_role_mgt_privileged_auth_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1019_role_mgt_privileged_role_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1019_role_mgt_privileged_role_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1020_role_mgt_security_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1020_role_mgt_security_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1021_role_mgt_security_operator(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1021_role_mgt_security_operator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1022_role_mgt_security_reader(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1022_role_mgt_security_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output


def entraid_p1023_role_mgt_user_admin(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(entra_kql_path,
                               'entraid_p1023_role_mgt_user_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='TimeGenerated')
    else:
        output = f'type={type} not supported'

    return output

