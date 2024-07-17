import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
mpath = os.path.join(cpath, 'mde')


def pwsht1003_pid_0001_export_sam(*, logic='mde', lookback='1d'):
    """
    PowerShell Registry Command

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'pwsht1003_pid_0001_export_sam.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pwsht1003_pid_0002_export_security(*, logic='mde', lookback='1d'):
    """
    PowerShell Registry Command

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'pwsht1003_pid_0002_export_security.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pwsht1003_pid_0003_export_system(*, logic='mde', lookback='1d'):
    """
    PowerShell Registry Command

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'pwsht1003_pid_0003_export_system.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pwsht1003_pid_0004_export_lsa_secrets(*, logic='mde', lookback='1d'):
    """
    PowerShell Registry Command

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'pwsht1003_pid_0004_export_lsa_secrets.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query