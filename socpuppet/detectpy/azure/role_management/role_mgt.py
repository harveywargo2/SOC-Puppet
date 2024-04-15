import yaml
import os
import socpuppet as soc


def rolemgt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def rolemgt_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(rolemgt_path(), 'logic_azmon')
    return output


def rolemgt_p0001_any_global_admin(*, logic='azmon', lookback='1d'):
    """
    Any Global Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0001_any_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0002_any_global_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any Global Admin activity outside of PIM

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0002_any_global_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0003_any_app_admin(*, logic='azmon', lookback='1d'):
    """
    Any App Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0003_any_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_p0004_any_app_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Any App Admin activity

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0004_any_app_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query