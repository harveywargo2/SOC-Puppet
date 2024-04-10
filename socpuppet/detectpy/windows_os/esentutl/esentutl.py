import yaml
import os
import socpuppet as soc


def esent_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def esent_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(esent_path(), 'logic_mde')
    return output


def esentutl_p0001_copy_sam(*, logic='mde', lookback='1d'):
    """
    esentutl copy sam file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(esent_mde_path(),
                               'esentutl_pid_0001_copy_sam.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def esentutl_p0002_copy_ntds(*, logic='mde', lookback='1d'):
    """
    esentutl copy ntds file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(esent_mde_path(),
                               'esentutl_pid_0002_copy_ntds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def esentutl_p0003_create_vss(*, logic='mde', lookback='1d'):
    """
    esentutl create vss

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(esent_mde_path(),
                               'esentutl_pid_0003_create_vss.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def esentutl_p0004_webcache_browser_dump(*, logic='mde', lookback='1d'):
    """
    esentutl webcache browser dump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(esent_mde_path(),
                               'esentutl_pid_0004_webcache_browser_dump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query