import yaml
import os
import socpuppet as soc


def fedtrust_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def fedtrust_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(fedtrust_path(), 'logic_azmon')
    return output


def trust_pid_0001_federation_settings_modified(*, logic='azmon', lookback='1d'):
    """
    Federated Trust Settings Modified

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(fedtrust_azmon_path(),
                               'trust_pid_0001_federation_settings_modified.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

