import yaml
import os
import socpuppet as soc
from socpuppet.detectpy.attack_id.t1003.t1003 import t1003_mde_path as mde_path


def builtin_pid_0001_edr_steal_creds_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0001_edr_steal_creds_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0002_edr_process_memory_dump_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0002_edr_process_memory_dump_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0003_edr_cred_memory_read_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0003_edr_cred_memory_read_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0004_av_hacktool_atpminidump_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0004_av_hacktool_atpminidump_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0005_av_hacktool_atpminidump_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0005_av_hacktool_atpminidump_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0006_av_hacktool_atpminidump_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0006_av_hacktool_atpminidump_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0007_av_rundlllolbin_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0007_av_rundlllolbin_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0008_av_rundlllolbin_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0008_av_rundlllolbin_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0009_av_rundlllolbin_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0009_av_rundlllolbin_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query