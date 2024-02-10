import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
msdt_path = os.path.dirname(os.path.abspath(__file__))
msdt_kql_path = os.path.join(msdt_path, 'kql')
msdt_sigma_path = os.path.join(msdt_path, 'sigma')


def msdt_p1000_follina_0day(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(msdt_kql_path,
                               'msdt_p1000_follina_0day.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output


def msdt_p1001_pcwdiag_executing_xml(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(msdt_kql_path,
                               'msdt_p1001_pcwdiag_executing_xml.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output

