import yaml
import os
import socpuppet as soc


cpath = os.path.dirname(os.path.abspath(__file__))
azpath = os.path.join(cpath, 'azmon')


def logon_pid_0001_2625_status_logon_failure(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0001_2625_status_logon_failure.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0002_2625_status_acnt_disabled(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0002_2625_status_acnt_disabled.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0003_2625_status_invalid_logon_hrs(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0003_2625_status_invalid_logon_hrs.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0004_2625_status_no_such_user(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0004_2625_status_no_such_user.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0005_2625_status_invalid_acnt_name(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0005_2625_status_invalid_acnt_name.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0006_2625_status_wrong_pwd(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0006_2625_status_wrong_pwd.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0007_2625_status_acnt_restriction(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0007_2625_status_acnt_restriction.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0008_2625_status_smartcard_wrong_pin(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0008_2625_status_smartcard_wrong_pin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0009_2625_status_smartcard_blocked(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0009_2625_status_smartcard_blocked.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0010_2625_status_smartcard_not_authenticated(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0010_2625_status_smartcard_not_authenticated.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0011_4625_status_smartcard_no_card(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0011_4625_status_smartcard_no_card.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0012_4625_status_smartcard_no_key_container(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0012_4625_status_smartcard_no_key_container.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0013_4625_status_smartcard_no_certificates(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0013_4625_status_smartcard_no_certificates.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0014_4625_status_smartcard_no_keyset(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0014_4625_status_smartcard_no_keyset.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0015_4625_status_smartcard_card_expired(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0015_4625_status_smartcard_card_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0016_4625_status_pwd_expired(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0016_4625_status_pwd_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0017_4625_status_smartcard_logon_required(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0017_4625_status_smartcard_logon_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0018_4625_status_sync_required(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0018_4625_status_sync_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0019_4625_status_dc_time_diff(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0019_4625_status_dc_time_diff.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0020_4625_status_logon_type_note_granted(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0020_4625_status_logon_type_note_granted.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0021_4625_status_ltrusted_relationship_fail(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0021_4625_status_ltrusted_relationship_fail.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0022_4625_status_pwd_must_change(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0022_4625_status_pwd_must_change.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0023_4625_status_acnt_locked_out(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0023_4625_status_acnt_locked_out.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0024_4625_status_failure_single_ip(*, logic='azmon', lookback='1d'):
    """
    Logon

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(azpath,
                               'logon_pid_0024_4625_status_failure_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query