import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def kerb_pid_0001_4768_kdc_err_c_principal_unknown(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0001_4768_kdc_err_c_principal_unknown.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0002_4768_kdc_err_policy(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0002_4768_kdc_err_policy.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0003_4768_kdc_err_client_revoked(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0003_4768_kdc_err_client_revoked.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0004_4768_kdc_err_key_expired(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0004_4768_kdc_err_key_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0005_4768_kdc_local_auth_success(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0005_4768_kdc_local_auth_success.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0006_4768_kdc_local_auth_failure(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0006_4768_kdc_local_auth_failure.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0007_4768_kdc_logon_without_pre_auth(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0007_4768_kdc_logon_without_pre_auth.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0008_4768_kdc_err_c_principal_single_ip(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0008_4768_kdc_err_c_principal_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0009_4771_kdc_err_c_principal_unknown(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0009_4771_kdc_err_c_principal_unknown.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0010_4771_kdc_err_policy(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0010_4771_kdc_err_policy.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0011_4771_kdc_err_client_revoked(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0011_4771_kdc_err_client_revoked.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0012_4771_kdc_err_key_expired(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0012_4771_kdc_err_key_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0013_4771_kdc_err_preauth_failed(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0013_4771_kdc_err_preauth_failed.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def kerb_pid_0014_4771_kdc_err_preauth_failed_single_ip(*, logic='azmon', lookback='1d'):
    """
    Kerberos Ticketing System

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'kerb_pid_0014_4771_kdc_err_preauth_failed_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query