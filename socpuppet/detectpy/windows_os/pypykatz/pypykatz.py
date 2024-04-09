import yaml
import os
import socpuppet as soc


def pykatz_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def pykatz_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(pykatz_path(), 'logic_mde')
    return output


def pypykatz_pid_0001_live_lsa(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for LSASS dumps

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0001_live_lsa.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0002_live_lsa_write_outfile(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for LSASS dumps writing to an output file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0002_live_lsa_write_outfile.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0003_live_registry(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for sam file dumps

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0003_live_registry.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0004_live_registry_write_outfile(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for sam file dumps write to file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0004_live_registry_write_outfile.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0005_live_dcsync(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for dcsync

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0005_live_dcsync.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0007_live_regdump(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for regdump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0007_live_regdump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0008_live_lsassdump(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for lsassdump

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0008_live_lsassdump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0009_live_shareenum(*, logic='mde', lookback='1d'):
    """
    Pypykatz commands for shareenum

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0009_live_shareenum.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def pypykatz_pid_0010_command_line_indicator(*, logic='mde', lookback='1d'):
    """
    Pypykatz indicator in command line

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(pykatz_mde_path(),
                                'pypykatz_pid_0010_command_line_indicator.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

