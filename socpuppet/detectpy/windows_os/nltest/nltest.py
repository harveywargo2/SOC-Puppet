import yaml
import os
import socpuppet as soc


def nltest_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def nltest_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(nltest_path(), 'logic_mde')
    return output


def nltest_pid_0001_dclist(*, logic='mde', lookback='1d'):
    """
    Nltest dclist command used

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(nltest_mde_path(),
                               'nltest_pid_0001_dclist.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def nltest_pid_0002_domain_trusts(*, logic='mde', lookback='1d'):
    """
    Nltest /domain_trusts command used

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(nltest_mde_path(),
                               'nltest_pid_0002_domain_trusts.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def nltest_pid_0003_trusted_domains(*, logic='mde', lookback='1d'):
    """
    Nltest /trusted_domains command used

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(nltest_mde_path(),
                               'nltest_pid_0003_trusted_domains.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def nltest_pid_0004_dsgetdc(*, logic='mde', lookback='1d'):
    """
    Nltest /dsgetdc command used

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(nltest_mde_path(),
                               'nltest_pid_0004_dsgetdc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

