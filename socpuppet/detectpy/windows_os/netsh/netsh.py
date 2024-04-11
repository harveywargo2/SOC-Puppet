import yaml
import os
import socpuppet as soc


def netsh_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def netsh_mde_path():
    """
    :return: Absolute Path for MDE Logic Lib
    """
    output = os.path.join(netsh_path(), 'logic_mde')
    return output


def netsh_pid_0001_set_firewall_profile_off(*, logic='mde', lookback='1d'):
    """
    netsh command to set any firewall profile off

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0001_set_firewall_profile_off.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0002_disable_windows_firewall(*, logic='mde', lookback='1d'):
    """
    netsh command to disable windows firewall

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0002_disable_windows_firewall.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0003_file_rename(*, logic='mde', lookback='1d'):
    """
    netsh file renames

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0003_file_rename.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0004_mod_firewall_rdp_enable(*, logic='mde', lookback='1d'):
    """
    netsh enable rdp

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0004_mod_firewall_rdp_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0005_mod_firewall_smb_enable(*, logic='mde', lookback='1d'):
    """
    netsh enable smb

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0005_mod_firewall_smb_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0006_add_fw_rule(*, logic='mde', lookback='1d'):
    """
    netsh add firewall rule

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0006_add_fw_rule.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0007_add_fw_rule_rdp(*, logic='mde', lookback='1d'):
    """
    netsh add firewall rule rdp

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0007_add_fw_rule_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0008_show_fw_rules(*, logic='mde', lookback='1d'):
    """
    netsh show firewall rules

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0008_show_fw_rules.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0009_helper_dll(*, logic='mde', lookback='1d'):
    """
    netsh helper dll

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0009_helper_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0010_port_forwarding(*, logic='mde', lookback='1d'):
    """
    netsh port forwarding

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0010_port_forwarding.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0011_port_forwarding_rdp(*, logic='mde', lookback='1d'):
    """
    netsh port forwarding rdp

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0011_port_forwarding_rdp.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def netsh_pid_0012_port_proxy(*, logic='mde', lookback='1d'):
    """
    netsh port proxy

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(netsh_mde_path(),
                               'netsh_pid_0012_port_proxy.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query