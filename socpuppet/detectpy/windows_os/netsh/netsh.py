import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
netsh_path = os.path.dirname(os.path.abspath(__file__))
netsh_kql_path = os.path.join(netsh_path, 'kql')
netsh_sigma_path = os.path.join(netsh_path, 'sigma')


def netsh_p0001_disable_windows_firewall(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p0001_disable_windows_firewall.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p0002_disable_windows_firewall(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p0002_disable_windows_firewall.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p1000_mod_firewall_rules_rdp_enable(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p1000_mod_firewall_rule_rdp_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p1001_mod_firewall_rules_smb_enable(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p1001_mod_firewall_rule_smb_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p1002_mod_firewall_service_rdp_enable(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p1002_mod_firewall_service_rdp_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p1003_mod_firewall_rule_network_discovery_enable(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p1003_mod_firewall_rule_network_discovery_enable.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def netsh_p2000_add_rule(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(netsh_kql_path,
                               'netsh_p2000_add_rule.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output

