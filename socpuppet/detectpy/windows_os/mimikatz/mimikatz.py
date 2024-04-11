import yaml
import os
import socpuppet as soc


def mk_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def mk_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(mk_path(), 'logic_mde')
    return output


def mimikatz_pid_0001_file_ioc(*, logic='mde', lookback='1d'):
    """
    Mimikatz Keyword Found in File Event

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0001_file_ioc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0002_process_ioc(*, logic='mde', lookback='1d'):
    """
    Mimikatz Keyword Found in Process Create

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0002_process_ioc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0003_sekurlsa(*, logic='mde', lookback='1d'):
    """
    Mimikatz sekurlsa command indicator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0003_sekurlsa.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0004_lsadump(*, logic='mde', lookback='1d'):
    """
    Mimikatz lsadump command indicator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0004_lsadump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0005_privilege(*, logic='mde', lookback='1d'):
    """
    Mimikatz privilege command

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0005_privilege.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0006_kerberos(*, logic='mde', lookback='1d'):
    """
    Mimikatz kerberos command

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0006_kerberos.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0007_crypto(*, logic='mde', lookback='1d'):
    """
    Mimikatz crypto commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0007_crypto.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0008_vault(*, logic='mde', lookback='1d'):
    """
    Mimikatz vault commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0008_vault.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0009_dpapi(*, logic='mde', lookback='1d'):
    """
    Mimikatz dpapi commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0009_dpapi.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0010_process(*, logic='mde', lookback='1d'):
    """
    Mimikatz process commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0010_process.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query



def mimikatz_pid_0011_misc(*, logic='mde', lookback='1d'):
    """
    Mimikatz misc commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0011_misc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0012_rpc(*, logic='mde', lookback='1d'):
    """
    Mimikatz rpc commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0012_rpc.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mimikatz_pid_0013_event(*, logic='mde', lookback='1d'):
    """
    Mimikatz event commands

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mk_mde_path(),
                               'mimikatz_pid_0013_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

