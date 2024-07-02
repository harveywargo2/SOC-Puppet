import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def user_pid_0001_mfa_susp_activity_reported(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'user_pid_0001_mfa_susp_activity_reported.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def user_pid_0002_mfa_fraud_reported(*, logic='azmon', lookback='1d'):
    """
    Azure Builtin Roles

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'user_pid_0002_mfa_fraud_reported.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query