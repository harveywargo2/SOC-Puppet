import yaml
import os
import socpuppet as soc
from socpuppet.detectpy.attack_id.t1003.t1003 import t1003_mde_path as mde_path


def procdump_pid_0001_minidump_flag(*, logic='mde', lookback='1d'):
    """
    procdump

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'procdump_pid_0001_minidump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0002_minidump_flag_lsass(*, logic='mde', lookback='1d'):
    """
    procdump

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'procdump_pid_0002_minidump_flag_lsass.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0003_fulldump_flag(*, logic='mde', lookback='1d'):
    """
    procdump

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'procdump_pid_0003_fulldump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0004_fulldump_flag_lsass(*, logic='mde', lookback='1d'):
    """
    procdump

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'procdump_pid_0004_fulldump_flag_lsass.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0005_any_dump_flag(*, logic='mde', lookback='1d'):
    """
    procdump

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'procdump_pid_0005_any_dump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

