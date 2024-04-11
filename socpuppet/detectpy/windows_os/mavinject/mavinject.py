import yaml
import os
import socpuppet as soc


def mavinject_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def mavinject_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(mavinject_path(), 'logic_mde')
    return output


def mavinject_pid_0001_inject_dll(*, logic='mde', lookback='1d'):
    """
    mavinject inject dll

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mavinject_mde_path(),
                               'mavinject_pid_0001_inject_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query