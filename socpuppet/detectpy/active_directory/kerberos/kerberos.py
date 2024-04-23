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


def kerb_pid_0001_4768_kdc_err_c_principal_unknown(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Auth Fail

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0001_4768_kdc_err_c_principal_unknown.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0002_4768_kdc_err_policy(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Auth Fail

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0002_4768_kdc_err_policy.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0003_4768_kdc_err_client_revoked(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Auth Fail

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0003_4768_kdc_err_client_revoked.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0004_4768_kdc_err_key_expired(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Auth Fail

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0004_4768_kdc_err_key_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0005_4768_kdc_local_auth_success(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Local Auth Success

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0005_4768_kdc_local_auth_success.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0006_4768_kdc_local_auth_failure(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Local Auth Failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0006_4768_kdc_local_auth_failure.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0007_4768_kdc_logon_without_pre_auth(*, logic='azmon', lookback='1d'):
    """
    4768 Kerb Ticket Without Pre Auth

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(kerb_azmon_path(),
                               'kerb_pid_0007_4768_kdc_logon_without_pre_auth.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query