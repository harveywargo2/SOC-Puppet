import yaml
import os
import socpuppet as soc


def uam_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def uam_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(uam_path(), 'logic_azmon')
    return output


def uam_pid_0001_4738_user_normal_account_dont_expire_password(*, logic='azmon', lookback='1d'):
    """
    4738 User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(uam_azmon_path(),
                               'uam_pid_0001_4738_user_normal_account_dont_expire_password.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def uam_pid_0002_4738_user_normal_account_password_not_required(*, logic='azmon', lookback='1d'):
    """
    4738 User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(uam_azmon_path(),
                               'uam_pid_0002_4738_user_normal_account_password_not_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def uam_pid_0003_4738_user_normal_account_password_not_required_dont_expire_password(*, logic='azmon', lookback='1d'):
    """
    4738 User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(uam_azmon_path(),
                               'uam_pid_0003_4738_user_normal_account_password_not_required_dont_expire_password.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query