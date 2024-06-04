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
                               'comsvcs_pid_001_created_minidump'), 'r') as file:
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

