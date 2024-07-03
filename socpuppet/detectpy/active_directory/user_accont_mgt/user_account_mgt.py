import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def uam_pid_0001_4738_user_normal_acnt_dont_expire_pwd(*, logic='azmon', lookback='1d'):
    """
    User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'uam_pid_0001_4738_user_normal_acnt_dont_expire_pwd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def uam_pid_0002_4738_user_normal_acnt_pwd_not_required(*, logic='azmon', lookback='1d'):
    """
    User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'uam_pid_0002_4738_user_normal_acnt_pwd_not_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def uam_pid_0003_4738_user_normal_acnt_pwd_not_required_dont_expire(*, logic='azmon', lookback='1d'):
    """
    User Account Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'uam_pid_0003_4738_user_normal_acnt_pwd_not_required_dont_expire.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query