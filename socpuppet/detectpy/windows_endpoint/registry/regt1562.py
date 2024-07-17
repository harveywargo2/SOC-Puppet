import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
mpath = os.path.join(cpath, 'mde')


def regt1562_pid_0001_netntlm_downgrade_restrict_sending_ntlm_traffic(*, logic='mde', lookback='1d'):
    """
    NetNTLM Downgrade Attack

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mpath,
                               'regt1562_pid_0001_netntlm_downgrade_restrict_sending_ntlm_traffic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

