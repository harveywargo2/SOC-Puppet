import os
import yaml



# Path Variables for Module
mod_path = os.path.dirname(os.path.abspath(__file__))
kql_path = os.path.join(mod_path, 'kql')
sigma_path = os.path.join(mod_path, 'sigma')


def net_utl_group_cmd_run(x='1d'):
    with open(os.path.join(kql_path, 'Net_Utility_Group_Command_Run.yaml'), 'r') as file:
        data = yaml.safe_load(file)

    logic = data.get('kqlTable') + f'| where Timestamp >= ago({x})' + data.get('kqlQuery')
    logic_dict = {'query': logic}

    return logic_dict

