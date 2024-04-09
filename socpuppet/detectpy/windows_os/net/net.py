import yaml
import os
import socpuppet as soc


def net_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def net_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(net_path(), 'logic_mde')
    return output


def net_pid_0001_output_redirected_to_file(*, logic='mde', lookback='1d'):
    """
    NET command output saved/redirected to file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0001_output_redirected_to_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0002_created_modified_file(*, logic='mde', lookback='1d'):
    """
    NET created a file

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0002_created_modified_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0003_domain_group(*, logic='mde', lookback='1d'):
    """
    NET with /dom and group flags

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0003_domain_group.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0004_domain_group_domain_admins(*, logic='mde', lookback='1d'):
    """
    NET group list users in Domain Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0004_domain_group_domain_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0005_domain_group_domain_admins_add(*, logic='mde', lookback='1d'):
    """
    NET group add users in Domain Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0005_domain_group_domain_admins_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0006_domain_group_enterprise_admins(*, logic='mde', lookback='1d'):
    """
    NET group list users in Enterprise Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0006_domain_group_enterprise_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query