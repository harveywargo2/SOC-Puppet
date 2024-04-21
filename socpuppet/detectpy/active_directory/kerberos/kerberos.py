import yaml
import os
import socpuppet as soc


def kerb_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def kerb_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(kerb_path(), 'logic_azmon')
    return output


def kerb_pid_0001_4768_fail_bad_acnt_single_ip(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Auth Fail w/ bad account from single IP

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0001_4768_fail_bad_acnt_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0002_4771_fail_bad_pword_single_ip(*, logic='azmon', lookback='1d'):
    """
    4771 Kerb Auth Fail w/ bad account from single IP

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0002_4771_fail_bad_pword_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query