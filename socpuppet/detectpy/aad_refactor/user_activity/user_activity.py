import yaml
import os
import socpuppet as soc


def user_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def user_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(user_path(), 'logic_azmon')
    return output


def user_pid_0001_mfa_suspicious_activity_reported(*, logic='azmon', lookback='1d'):
    """
    User MFA Activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(user_azmon_path(),
                               'user_pid_0001_mfa_suspicious_activity_reported.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def user_pid_0002_mfa_fraud_reported(*, logic='azmon', lookback='1d'):
    """
    User MFA Activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(user_azmon_path(),
                               'user_pid_0002_mfa_fraud_reported.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

