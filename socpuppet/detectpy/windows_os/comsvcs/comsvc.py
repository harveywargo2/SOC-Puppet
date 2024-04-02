import yaml
import os
import socpuppet as soc


def comsvcs_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def comsvcs_mde_path():
    """
    :return: Absolute Path CMSTP MDE Logic Lib
    """
    output = os.path.join(comsvcs_path(), 'logic_mde')
    return output


def comsvcs_p0001_created_minidump(*, logic='mde', lookback='1d'):
    """
    Rundll Called Comsvcs to create a minidump of process

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(comsvcs_mde_path(),
                                'comsvcs_pid_0001_created_minidump.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_p0002_minidumpw_function_call(*, logic='mde', lookback='1d'):
    """
    Rundll Called Comsvcs and called function #24 MiniDumpW

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(comsvcs_mde_path(),
                                'comsvcs_pid_0002_minidumpw_function_call.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def comsvcs_p0003_created_file(*, logic='mde', lookback='1d'):
    """
    Comsvcs created or modified a file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(comsvcs_mde_path(),
                                'comsvcs_pid_0002_minidumpw_function_call.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query