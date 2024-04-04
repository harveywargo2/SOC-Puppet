import yaml
import os
import socpuppet as soc


def mshta_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def mshta_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(mshta_path(), 'logic_mde')
    return output


def mshta_pid_0001_executing_hta(*, logic='mde', lookback='1d'):
    """
    MSHTA executing HTA file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0001_executing_hta.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0002_executing_vbs(*, logic='mde', lookback='1d'):
    """
    MSHTA executing vbs script

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0002_executing_vbs.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0003_executing_javascript(*, logic='mde', lookback='1d'):
    """
    MSHTA executing Javascript

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0003_executing_javascript.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0004_executing_remote_file(*, logic='mde', lookback='1d'):
    """
    MSHTA remote file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0004_executing_remote_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0005_rare_parent(*, logic='mde', lookback='1d'):
    """
    MSHTA spawned from rare parent/initiating process file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0005_rare_parent.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0006_rare_execution_folder(*, logic='mde', lookback='1d'):
    """
    MSHTA executing file in rare folder path location

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0006_rare_execution_folder.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0007_lethal_hta(*, logic='mde', lookback='1d'):
    """
    MSHTA spawned from svchost lethalhta

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0007_lethal_hta.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0008_rare_process_spawn(*, logic='mde', lookback='1d'):
    """
    MSHTA spawned from svchost lethalhta

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0008_rare_process_spawn.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0009_rare_shell_spawn(*, logic='mde', lookback='1d'):
    """
    MSHTA spawned cmd shell

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0009_rare_shell_spawn.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def mshta_pid_0010_rare_file_execution(*, logic='mde', lookback='1d'):
    """
    MSHTA executing a rare file like doc, xls, etc

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(mshta_mde_path(),
                                'mshta_pid_0010_rare_file_execution.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query