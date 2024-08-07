import pandas as pd
import yaml
from socpuppet.detectpy import detectpy_path
import os


def yaml_file_list():
    yaml_df = []
    for root, path, files in os.walk(detectpy_path()):
        for file in files:
            if file.endswith('.yaml'):
                yaml_df.append(os.path.join(root, file))

    return yaml_df


def yaml_to_df():

    data_list = yaml_file_list()
    output_df = pd.DataFrame(columns=['title', 'description', 'detectType', 'detectCon', 'detectLanguage',
                                      'tags', 'attackTechnique', 'attackSoftware', 'references', 'pattern',
                                      'dataSource', 'dataType', 'dataCollector', 'dataForwardTo', 'dataparser',
                                      'dataParser', 'dataStorage', 'dataTable', 'dataIndex', 'dataAccess', 'dataMap',
                                      'kqlVar', 'kqlTable', 'kqlQuery'])

    df_index = 0


    for item in data_list:
        with open(item, 'r') as yaml_stream:
            yaml_dict = yaml.safe_load(yaml_stream)
        df_index += 1

        output_df.loc[df_index, 'title'] = yaml_dict['detect']['title']
        output_df.loc[df_index, 'description'] = yaml_dict['detect']['description']
        output_df.loc[df_index, 'detectType'] = yaml_dict['detect']['detectType']
        output_df.loc[df_index, 'detectCon'] = yaml_dict['detect']['detectCon']
        output_df.loc[df_index, 'detectLanguage'] = yaml_dict['detect']['detectLanguage']
        output_df.loc[df_index, 'tags'] = yaml_dict['intel']['tags']
        output_df.loc[df_index, 'attackTechnique'] = yaml_dict['intel']['attackId']
        output_df.loc[df_index, 'references'] = yaml_dict['intel']['references']
        output_df.loc[df_index, 'pattern'] = yaml_dict['intel']['pattern']
        output_df.loc[df_index, 'dataSource'] = yaml_dict['dataRequirements']['dataSource']
        output_df.loc[df_index, 'dataType'] = yaml_dict['dataRequirements']['dataType']
        output_df.loc[df_index, 'dataCollector'] = yaml_dict['dataRequirements']['dataCollector']
        output_df.loc[df_index, 'dataForwardTo'] = yaml_dict['dataRequirements']['dataForwardTo']
        output_df.loc[df_index, 'dataStorage'] = yaml_dict['dataRequirements']['dataStorage']
        output_df.loc[df_index, 'dataTable'] = yaml_dict['dataRequirements']['dataTable']
        output_df.loc[df_index, 'dataIndex'] = yaml_dict['dataRequirements']['dataIndex']
        output_df.loc[df_index, 'dataAccess'] = yaml_dict['dataRequirements']['dataAccess']
        output_df.loc[df_index, 'dataMap'] = yaml_dict['dataRequirements']['dataMap']
        output_df.loc[df_index, 'kqlVar'] = yaml_dict['logic']['kqlVar']
        output_df.loc[df_index, 'kqlTable'] = yaml_dict['logic']['kqlTable']
        output_df.loc[df_index, 'kqlQuery'] = yaml_dict['logic']['kqlQuery']


    return output_df


def detectpy_index():
    output = yaml_to_df()

    return output


detectpy_index().to_csv('detectpy_index.csv')


def detectpy_index():
    output = yaml_to_df()

    return output


detectpy_index().to_csv('detectpy_index.csv')