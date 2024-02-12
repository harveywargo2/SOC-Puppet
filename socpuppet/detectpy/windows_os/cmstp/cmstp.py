import os
import yaml
import socpuppet.detectpy.kql_qbuild as kbuild


# Path Variables for Module
cmstp_path = os.path.dirname(os.path.abspath(__file__))
cmstp_kql_path = os.path.join(cmstp_path, 'kql')
cmstp_sigma_path = os.path.join(cmstp_path, 'sigma')


def cmstp_p1000_executing_inf_file(*, type='kql', kql_ago='1d'):

    if type == 'kql':
        with open(os.path.join(cmstp_kql_path,
                               'cmstp_p1000_executing_inf_file.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        output = kbuild.kql_single_table_builder(data, kql_ago, time_field='Timestamp')
    else:
        output = f'type={type} not supported'

    return output

