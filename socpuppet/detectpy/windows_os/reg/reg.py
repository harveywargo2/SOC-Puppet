import yaml
import os
import socpuppet as soc


def reg_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def reg_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(reg_path(), 'logic_mde')
    return output


def reg_pid_0001_hklm_sam_save(*, logic='mde', lookback='1d'):
    """
    Reg.exe saving SAM file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(reg_mde_path(),
                               'reg_pid_0001_hklm_sam_save.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def reg_pid_0002_hklm_system_save(*, logic='mde', lookback='1d'):
    """
    Reg.exe saving system file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(reg_mde_path(),
                               'reg_pid_0002_hklm_system_save.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def reg_pid_0003_hklm_security_save(*, logic='mde', lookback='1d'):
    """
    Reg.exe saving Security file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(reg_mde_path(),
                               'reg_pid_0003_hklm_security_save.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def reg_pid_0004_hklm_lsa_secrets_save(*, logic='mde', lookback='1d'):
    """
    Reg.exe dumping LSA secrets

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(reg_mde_path(),
                               'reg_pid_0004_hklm_lsa_secrets_save.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query

