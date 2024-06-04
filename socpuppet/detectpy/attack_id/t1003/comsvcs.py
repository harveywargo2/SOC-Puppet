import yaml
import os
import socpuppet as soc
from socpuppet.detectpy.attack_id.t1003.t1003 import t1003_mde_path as mde_path


def comsvcs_pid_0001_created_minidump(*, logic='mde', lookback='1d'):
    """
    comsvcs

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0001_created_minidump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_pid_0002_called_minidumpw_function(*, logic='mde', lookback='1d'):
    """
    comsvcs

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0002_called_minidumpw_function.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_pid_0003_created_file(*, logic='mde', lookback='1d'):
    """
    comsvcs

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0003_created_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_pid_0004_av_rundlllolbin_alert(*, logic='mde', lookback='1d'):
    """
    MDE AV RunDllLolBin

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0004_av_rundlllolbin_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_pid_0005_av_rundlllolbin_event(*, logic='mde', lookback='1d'):
    """
    MDE AV RunDllLolBin

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0005_av_rundlllolbin_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_pid_0006_av_rundlllolbin_dynamic(*, logic='mde', lookback='1d'):
    """
    MDE AV RunDllLolBin

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'comsvcs_pid_0006_av_rundlllolbin_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query