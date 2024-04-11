import yaml
import os
import socpuppet as soc


def msdt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def msdt_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(msdt_path(), 'logic_mde')
    return output


def msdt_pid_0001_follina_rce_exploit(*, logic='mde', lookback='1d'):
    """
    MSDT Follina RCE Exploit Attempt

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(msdt_mde_path(),
                               'msdt_pid_0001_follina_rce_exploit.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def msdt_pid_0002_pcwdiag_executing_xml(*, logic='mde', lookback='1d'):
    """
    MSDT pcwdiag executing xml

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(msdt_mde_path(),
                               'msdt_pid_0002_pcwdiag_executing_xml.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

