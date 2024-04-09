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


def net_pid_0003_group_domain(*, logic='mde', lookback='1d'):
    """
    NET with /dom and group flags

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0003_group_domain.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0004_group_domain_admins(*, logic='mde', lookback='1d'):
    """
    NET group list users in Domain Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0004_group_domain_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0005_group_domain_admins_add(*, logic='mde', lookback='1d'):
    """
    NET group add users in Domain Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0005_group_domain_admins_add.yaml'), 'r') as file:
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
                                'net_pid_0006_group_enterprise_admins.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0007_group_enterprise_admins_add(*, logic='mde', lookback='1d'):
    """
    NET group add users to Enterprise Admins

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0007_group_enterprise_admins_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0008_file_rename(*, logic='mde', lookback='1d'):
    """
    NET command line utility renamed

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0008_file_rename.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0009_localgroup(*, logic='mde', lookback='1d'):
    """
    NET localgroup

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0009_localgroup.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0010_localgroup_add(*, logic='mde', lookback='1d'):
    """
    NET add user to localgroup

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0010_localgroup_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0011_localgroup_administrators(*, logic='mde', lookback='1d'):
    """
    NET localgroup administrators

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0011_localgroup_administrators.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0012_localgroup_administrators_add(*, logic='mde', lookback='1d'):
    """
    NET add user to local group administrators

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0012_localgroup_administrators_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0013_localgroup_rdp(*, logic='mde', lookback='1d'):
    """
    NET localgroup rdp

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0013_localgroup_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0014_localgroup_rdp_add(*, logic='mde', lookback='1d'):
    """
    NET localgroup rdp add

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0014_localgroup_rdp_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0015_user(*, logic='mde', lookback='1d'):
    """
    NET user command

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0015_user.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0016_user_add(*, logic='mde', lookback='1d'):
    """
    NET user command add

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0016_user_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0017_user_domain_add(*, logic='mde', lookback='1d'):
    """
    NET add user command with domain flag

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0017_user_domain_add.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0018_user_password_not_expire(*, logic='mde', lookback='1d'):
    """
    NET add user command with password no epire set

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0018_user_password_never_expire.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0019_user_passwordchg(*, logic='mde', lookback='1d'):
    """
    NET passwordchg

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0019_user_passwordchg.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0020_view(*, logic='mde', lookback='1d'):
    """
    NET view

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0020_view.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0021_view_all(*, logic='mde', lookback='1d'):
    """
    NET view /all command

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0021_view_all.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def net_pid_0022_stop_defender(*, logic='mde', lookback='1d'):
    """
    NET stop defender

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open( os.path.join(net_mde_path(),
                                'net_pid_0022_stop_defender.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query