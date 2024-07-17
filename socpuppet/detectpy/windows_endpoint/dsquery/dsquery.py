import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
mpath = os.path.join(cpath, 'mde')


def dsquery_pid_0001_domain_trust(*, logic='mde', lookback='1d'):
    """
    dsquery

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'dsquery_pid_0001_domain_trust.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query