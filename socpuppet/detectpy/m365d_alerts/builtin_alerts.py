import yaml
import os
import socpuppet as soc


def defender_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def defender_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(defender_path(), 'logic_mde')
    return output


def builtin_pid_0001_t1003_alerts(*, logic='mde', lookback='1d'):
    """
    Defender builtin alerts for T1003 Cred Dumping

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(defender_mde_path(),
                                'builltin_pid_0001_t1003_alerts.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0002_msdt_follina_alerts(*, logic='mde', lookback='1d'):
    """
    Defender Builtin alerts for MSDT Follina CVE-2022-30190

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(defender_mde_path(),
                                'builltin_pid_msdt_follina_alerts.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0003_gsecdump(*, logic='mde', lookback='1d'):
    """
    Defender Builtin alerts for GSECDump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(defender_mde_path(),
                                'builltin_pid_0003_gsecdump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

