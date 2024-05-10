import yaml
import os
import socpuppet as soc


def lsass_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def lsass_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(lsass_path(), 'logic_mde')
    return output


def lsass_pid_0001_memory_read_not_system(*, logic='mde', lookback='1d'):
    """
    lsass memory read

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0001_memory_read_not_system.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def lsass_pid_0002_large_rare_memory_read(*, logic='mde', lookback='1d'):
    """
    lsass memory read

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0002_large_rare_memory_read.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def lsass_pid_0003_large_memory_read_rundll(*, logic='mde', lookback='1d'):
    """
    lsass memory read

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0003_large_memory_read_rundll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def lsass_pid_0004_large_memory_read_taskmgr(*, logic='mde', lookback='1d'):
    """
    lsass memory read

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0004_large_memory_read_taskmgr.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def lsass_pid_0005_dmp_file_created(*, logic='mde', lookback='1d'):
    """
    lsass memory read & dump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0005_dmp_file_created.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def lsass_pid_0006_dmp_file_created_pshell_get_process(*, logic='mde', lookback='1d'):
    """
    lsass memory dump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(lsass_mde_path(),
                               'lsass_pid_0006_dmp_file_created_pshell_get_process.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

