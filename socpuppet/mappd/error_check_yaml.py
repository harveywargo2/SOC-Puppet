import os
import yaml
from socpuppet.mappd.mappd import yaml_file_list


def yaml_to_df_error_chk():

    data_list = yaml_file_list()

    df_index = 0

    match_check = ['detect', 'title', 'description', 'detectType', 'detectLanguage', 'detectCon', 'urgency',
                   'inTheWild', 'noiseProjection', 'regressionVolume', 'analysisEffort', 'confidence', 'intel', 'tags',
                   'attackId', 'references', 'emulation', 'pattern', 'dataRequirements', 'dataSource', 'dataType',
                   'dataCollector', 'dataForwardTo', 'dataParser', 'dataStorage', 'dataTable', 'dataIndex',
                   'dataAccess', 'dataMap', 'logic', 'kqlVar', 'kqlTable', 'kqlQuery'
                   ]


    for item in data_list:
        with open(item, 'r') as yaml_stream:
            yaml_dict = yaml.safe_load(yaml_stream)
        df_index += 1


        key_list = []

        for key, value in yaml_dict.items():
            key_list.append(key)
            if isinstance(value, dict):
                key_list.extend(value)

        common_keys = list(set(key_list) & set(match_check))

        len_check = len(match_check)
        len_keys = len(common_keys)

        if len_check != len_keys:
            print('Error In: ', item)
            print(set(key_list) - set(match_check))

    return

yaml_to_df_error_chk()