import yaml
import os
import socpuppet as soc


def infd_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def infd_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(infd_path(), 'logic_mde')
    return output


def infdefaultinstall_pid_0001_executing_inf(*, logic='mde', lookback='1d'):
    """
    infdefaultinstall executing inf

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(infd_mde_path(),
                               'infdefaultinstall_pid_0001_executing_inf.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

