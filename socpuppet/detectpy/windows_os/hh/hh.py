import yaml
import os
import socpuppet as soc


def hh_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def hh_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(hh_path(), 'logic_mde')
    return output


def hh_pid_0001_executing_ps1(*, logic='mde', lookback='1d'):
    """
    hh executing ps1

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(hh_mde_path(),
                               'hh_pid_0001_executing_ps1.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def hh_pid_0002_executing_chm(*, logic='mde', lookback='1d'):
    """
    hh executing chm

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(hh_mde_path(),
                               'hh_pid_0002_executing_chm.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def hh_pid_0003_executing_remote_file(*, logic='mde', lookback='1d'):
    """
    hh executing remote file

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(hh_mde_path(),
                               'hh_pid_0003_executing_remote_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def hh_pid_0004_decompiling_file(*, logic='mde', lookback='1d'):
    """
    hh decompiling file

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(hh_mde_path(),
                               'hh_pid_0004_decompiling_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def hh_pid_0005_parent_file(*, logic='mde', lookback='1d'):
    """
    hh spawned from powershell

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(hh_mde_path(),
                               'hh_pid_0005_parent_powershell.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query