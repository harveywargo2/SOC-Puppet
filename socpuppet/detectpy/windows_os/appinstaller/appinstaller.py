import yaml
import os
import socpuppet as soc


def appin_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def appin_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(appin_path(), 'logic_mde')
    return output


def appinstaller_pid_0001_load_remote_package(*, logic='mde', lookback='1d'):
    """
    Appinstaller

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(appin_mde_path(),
                               'appinstaller_pid_0001_load_remote_package.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def appinstaller_pid_0002_handler_invoked_network_conn(*, logic='mde', lookback='1d'):
    """
    Appinstaller

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(appin_mde_path(),
                               'appinstaller_pid_0002_handler_invoked_network_conn.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

