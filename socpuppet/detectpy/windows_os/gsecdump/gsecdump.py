import yaml
import os
import socpuppet as soc


def gsd_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def gsd_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(gsd_path(), 'logic_mde')
    return output


def gsecdump_pid_0001_dump_memory(*, logic='mde', lookback='1d'):
    """
    gsecdump hacktool

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(gsd_mde_path(),
                               'gsecdump_pid_0001_dump_memory.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def gsecdump_pid_0002_file_indicator(*, logic='mde', lookback='1d'):
    """
    gsecdump hacktool

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(gsd_mde_path(),
                               'gsecdump_pid_0002_file_indicator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

