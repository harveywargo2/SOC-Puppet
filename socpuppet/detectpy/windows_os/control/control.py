import yaml
import os
import socpuppet as soc


def ctl_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def ctl_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(ctl_path(), 'logic_mde')
    return output


def control_pid_0001_executing_cpl_file(*, logic='mde', lookback='1d'):
    """
    Control executing cpl file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(ctl_mde_path(),
                               'control_pid_0001_executing_cpl_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def control_pid_0002_executing_dll_file(*, logic='mde', lookback='1d'):
    """
    Control executing dll

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(ctl_mde_path(),
                               'control_pid_0002_executing_dll_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def control_pid_0003_executing_file_via_rundll(*, logic='mde', lookback='1d'):
    """
    Control executing file via rundll

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(ctl_mde_path(),
                               'control_pid_0003_executing_file_via_rundll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

