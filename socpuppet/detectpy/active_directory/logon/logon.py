import yaml
import os
import socpuppet as soc


def logon_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def logon_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(logon_path(), 'logic_azmon')
    return output


def logon_pid_0001_4625_status_logon_failure(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0001_4625_status_logon_failure.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0002_4625_status_account_disabled(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0002_4625_status_account_disabled.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0003_4625_status_invalid_logon_hours(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0003_4625_status_invalid_logon_hours.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0004_4625_status_no_such_user(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0004_4625_status_no_such_user.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0005_4625_status_invalid_account_name(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0005_4625_status_invalid_account_name.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0006_4625_status_wrong_password(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0006_4625_status_wrong_password.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0007_4625_status_account_restriction(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0007_4625_status_account_restriction.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0008_4625_status_smartcard_wrong_pin(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0008_4625_status_smartcard_wrong_pin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0009_4625_status_smartcard_blocked(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0009_4625_status_smartcard_blocked.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0010_4625_status_smartcard_card_not_authenticated(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0010_4625_status_smartcard_card_not_authenticated.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0011_4625_status_smartcard_no_card(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0011_4625_status_smartcard_no_card.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0012_4625_status_smartcard_no_key_container(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0012_4625_status_smartcard_no_key_container.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0013_4625_status_smartcard_no_certificates(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0013_4625_status_smartcard_no_certificates.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0014_4625_status_smartcard_no_keyset(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0014_4625_status_smartcard_no_keyset.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0015_4625_status_smartcard_cert_expired(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0015_4625_status_smartcard_cert_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0016_4625_status_password_expired(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0016_4625_status_password_expired.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0017_4625_status_smartcard_logon_required(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0017_4625_status_smartcard_logon_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0018_4625_status_synchronization_required(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0018_4625_status_synchronization_required.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0019_4625_status_time_difference_at_dc(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0019_4625_status_time_difference_at_dc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0020_4625_status_logon_type_not_granted(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0020_4625_status_logon_type_not_granted.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0021_4625_status_trusted_relationship_failure(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0021_4625_status_trusted_relationship_failure.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0022_4625_status_password_must_change(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0022_4625_status_password_must_change.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0023_4625_status_account_locked_out(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0023_4625_status_account_locked_out.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def logon_pid_0024_4625_status_logon_failure_single_ip(*, logic='azmon', lookback='1d'):
    """
    4625 status logon failure threshold met

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(logon_azmon_path(),
                               'logon_pid_0024_4625_status_logon_failure_single_ip.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query