import yaml
import os
import socpuppet as soc


def pd_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def pd_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(pd_path(), 'logic_mde')
    return output


def procdump_pid_0001_minidump_flag(*, logic='mde', lookback='1d'):
    """
    Procdump Creating MiniDump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0001_minidump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0002_minidump_lsass(*, logic='mde', lookback='1d'):
    """
    Procdump Creating MiniDump of LSASS

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0002_minidump_lsass.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0003_fulldump_flag(*, logic='mde', lookback='1d'):
    """
    Procdump Creating Fulldump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0003_fulldump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0004_fulldump_lsass(*, logic='mde', lookback='1d'):
    """
    Procdump Creating Fulldump of Lsass

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0004_fulldump_lsass.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0005_dump_flag(*, logic='mde', lookback='1d'):
    """
    Procdump With a Dump Flag

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0005_dump_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def procdump_pid_0006_renamed(*, logic='mde', lookback='1d'):
    """
    Procdump Renamed

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(pd_mde_path(),
                               'procdump_pid_0006_renamed.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

