import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def usermgt_pid_0001_user_add(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'usermgt_pid_0001_user_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0002_user_deleted(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'usermgt_pid_0002_user_deleted.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0003_user_hard_delete(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'usermgt_pid_0003_user_hard_delete.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0004_guest_user_invite(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'usermgt_pid_0004_guest_user_invite.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def usermgt_pid_0005_guest_invite_bulk_finished(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'usermgt_pid_0005_guest_invite_bulk_finished.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

