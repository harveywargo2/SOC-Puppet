import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def rolemgt_pid_0001_global_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0001_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0002_application_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0002_application_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0003_application_dev(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0003_application_dev.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0004_auth_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0004_auth_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0005_auth_policy_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0005_auth_policy_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0006_auth_extension_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0006_auth_extension_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0007_ief_keyset_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0007_ief_keyset_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0008_cloud_app_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0008_cloud_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0009_billing_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0009_billing_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0010_cloud_app_secuirty_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0010_cloud_app_secuirty_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0011_cloud_device_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0011_cloud_device_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0012_cap_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0012_cap_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0013_directory_reader(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0013_directory_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0014_directory_writer(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0014_directory_writer.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0015_domain_name_writer(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0015_domain_name_writer.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0016_exchange_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0016_exchange_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0017_directory_sync(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0017_directory_sync.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0018_global_reader(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0018_global_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0019_groups_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0019_groups_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0020_helpdesk_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0020_helpdesk_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0021_guest_inviter(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0021_guest_inviter.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0022_hybrid_id_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0022_hybrid_id_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0023_intune_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0023_intune_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0024_password_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0024_password_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0025_office_apps_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0025_office_apps_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query



def rolemgt_pid_0026_network_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0026_network_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0027_priv_role_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0027_priv_role_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0028_security_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0028_security_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0029_security_operator(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0029_security_operator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0030_priv_auth_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0030_priv_auth_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0031_security_reader(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0031_security_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0032_user_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0032_user_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0033_tier_support(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0033_tier_support.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0034_sharepoint_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0034_sharepoint_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0035_teams_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0035_teams_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0036_permissions_mgt_admin(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'rolemgt_pid_0036_permissions_mgt_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query