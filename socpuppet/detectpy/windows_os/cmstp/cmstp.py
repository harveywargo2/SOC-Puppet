import yaml
import os
import socpuppet as soc


def cmstp_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def cmstp_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(cmstp_path(), 'logic_mde')
    return output


def cmstp_pid_0001_executing_inf_file(*, logic='mde', lookback='1d'):
    """
    CMSTP Executing inf file

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0001_executing_inf_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def cmstp_pid_0002_executing_inf_file_silent_flag(*, logic='mde', lookback='1d'):
    """
    CMSTP Executing inf file with Silent Flag

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0002_executing_inf_file_silent_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def cmstp_pid_0003_executing_inf_file_all_profiles_flag(*, logic='mde', lookback='1d'):
    """
    CMSTP Executing inf file with All Profiles Flag

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0003_executing_inf_file_all_profiles_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def cmstp_pid_0004_executing_inf_file_single_user_flag(*, logic='mde', lookback='1d'):
    """
    CMSTP Executing inf file with Single User Flag

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0004_executing_inf_file_single_user_flag.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def cmstp_pid_0005_spawning_child_process(*, logic='mde', lookback='1d'):
    """
    CMSTP spawning child process

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0005_spawning_child_process.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def cmstp_pid_0006_rare_folder_path(*, logic='mde', lookback='1d'):
    """
    CMSTP Spawned from folder path that is not c:\Windows\System32

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(cmstp_mde_path(),
                               'cmstp_pid_0006_rare_folder_path.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

