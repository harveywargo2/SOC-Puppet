import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
mpath = os.path.join(cpath, 'mde')


def wuauclt_pid_0001_execute_dll(*, logic='mde', lookback='1d'):
    """
    cmstp

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'wuauclt_pid_0001_execute_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query