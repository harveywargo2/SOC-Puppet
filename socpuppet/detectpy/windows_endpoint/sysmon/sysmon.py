import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
mpath = os.path.join(cpath, 'mde')


def sysmon_pid_0001_uninstall(*, logic='mde', lookback='1d'):
    """
    fltmc

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'sysmon_pid_0001_uninstall.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query