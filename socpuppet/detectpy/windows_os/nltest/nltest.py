import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild

# Path Variables for Module
nltest_path = os.path.dirname(os.path.abspath(__file__))
nltest_kql_path = os.path.join(nltest_path, 'kql_m365d')
nltest_sigma_path = os.path.join(nltest_path, 'sigma')


def nltest_p1000_dclist_domain_controllers(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(nltest_kql_path,
                               'nltest_p1000_dclist_domain_controllers.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def nltest_p1001_domain_trusts(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(nltest_kql_path,
                               'nltest_p1001_domain_trusts.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def nltest_p1002_dsgetdc_list_dc_info(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(nltest_kql_path,
                               'nltest_p1002_dsgetdc_list_dc_info.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output


def nltest_p1003_trusted_domains(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(nltest_kql_path,
                               'nltest_p1003_trusted_domains.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output