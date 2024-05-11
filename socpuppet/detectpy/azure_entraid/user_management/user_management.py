import yaml
import os
import socpuppet as soc


def umgt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def umgt_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(umgt_path(), 'logic_azmon')
    return output


def usermgt_pid_0001_user_add(*, logic='azmon', lookback='1d'):
    """
    User Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(umgt_azmon_path(),
                               'usermgt_pid_0001_user_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0002_user_delete(*, logic='azmon', lookback='1d'):
    """
    User Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(umgt_azmon_path(),
                               'usermgt_pid_0002_user_delete.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0003_user_hard_delete(*, logic='azmon', lookback='1d'):
    """
    User Management

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(umgt_azmon_path(),
                               'usermgt_pid_0003_user_hard_delete.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

