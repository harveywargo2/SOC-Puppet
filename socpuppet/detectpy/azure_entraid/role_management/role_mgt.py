import yaml
import os
import socpuppet as soc


def rolemgt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def rolemgt_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(rolemgt_path(), 'logic_azmon')
    return output


def rolemgt_p0001_any_global_admin(*, logic='azmon', lookback='1d'):
    """
    Any Global Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0001_any_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0002_any_global_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any Global Admin Activity Outside of PIM

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0002_any_global_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0003_any_app_admin(*, logic='azmon', lookback='1d'):
    """
    Any App Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0003_any_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0004_any_app_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any App Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0004_any_app_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0005_any_app_dev(*, logic='azmon', lookback='1d'):
    """
    Any App Dev activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0005_any_app_dev.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0006_any_app_dev_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any App Dev activity no PIM

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0006_any_app_dev_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0007_any_auth_admin(*, logic='azmon', lookback='1d'):
    """
    Any auth admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0007_any_auth_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0008_any_auth_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any auth admin not PIM

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0008_any_auth_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0009_any_auth_policy_admin(*, logic='azmon', lookback='1d'):
    """
    Any auth policy admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0009_any_auth_policy_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0010_any_auth_policy_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any auth policy admin activity not from pim

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0010_any_auth_policy_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0011_any_auth_extension_admin(*, logic='azmon', lookback='1d'):
    """
    Any auth extension admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0011_any_auth_extension_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0012_any_auth_extension_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any auth extension admin activity not pim

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0012_any_auth_extension_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query