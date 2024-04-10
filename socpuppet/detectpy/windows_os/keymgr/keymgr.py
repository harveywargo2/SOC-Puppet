import yaml
import os
import socpuppet as soc


def km_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def km_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(km_path(), 'logic_mde')
    return output


def keymgr_pid_0001_cred_dump(*, logic='mde', lookback='1d'):
    """
    Key Manager User to Dump Creds

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(km_mde_path(), 'keymgr_pid_0001_cred_dump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

