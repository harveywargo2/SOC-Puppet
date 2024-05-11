import yaml
import os
import socpuppet as soc


def appc_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def appc_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(appc_path(), 'logic_mde')
    return output


def appcmd_pid_0001_list_svc_acnt_creds(*, logic='mde', lookback='1d'):
    """
    appcmd

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(appc_mde_path(),
                               'appcmd_pid_0001_list_svc_acnt_creds.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def appcmd_pid_0002_list_config(*, logic='mde', lookback='1d'):
    """
    appcmd

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(appc_mde_path(),
                               'appcmd_pid_0002_list_config.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query