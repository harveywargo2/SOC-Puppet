import yaml
import os
import socpuppet as soc


def wuauclt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def wuauclt_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(wuauclt_path(), 'logic_mde')
    return output


def wuauclt_pid_0001_execute_dll(*, logic='mde', lookback='1d'):
    """
    wuauclt

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(wuauclt_mde_path(),
                               'wuauclt_pid_0001_execute_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query