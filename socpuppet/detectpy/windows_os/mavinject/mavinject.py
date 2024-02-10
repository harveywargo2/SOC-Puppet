import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
mavinject_path = os.path.dirname(os.path.abspath(__file__))
mavinject_kql_path = os.path.join(mavinject_path, 'kql')
mavinject_sigma_path = os.path.join(mavinject_path, 'sigma')


def mavinject_p1000_inject_dll(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(mavinject_kql_path,
                               'mavinject_p1000_inject_dll.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago)
    else:
        output = f'type={type} not supported'

    return output