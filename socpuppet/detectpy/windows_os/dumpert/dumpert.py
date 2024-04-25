import yaml
import os
import socpuppet as soc


def dumpert_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def dumpert_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(dumpert_path(), 'logic_mde')
    return output


def dumpert_pid_0001_direct_api_call(*, logic='mde', lookback='1d'):
    """
    dumpert

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(dumpert_mde_path(),
                               'dumpert_pid_0001_direct_api_call.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

