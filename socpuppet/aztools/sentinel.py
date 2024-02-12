import requests
import socpuppet as soc
import pandas as pd
import json
from datetime import datetime


def azmonitor_oath_token(*, tenant_id, client_id, client_secret):
    auth_resp = soc.aztools.oauth_azure_monitor(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    auth_token = soc.aztools.oauth_bearer_token(auth_resp)
    return auth_token


def azmonitor_run_query(*, token, workspace_id, query_data):
    api_call_url = f'https://api.loganalytics.azure.com/v1/workspaces/{workspace_id}/query'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    api_call_response = requests.request('POST', api_call_url, headers=headers, json=query_data).json()

    return api_call_response


def azmonitor_run_query_df(*, token, workspace_id, query_data):
    data = azmonitor_run_query(token=token, workspace_id=workspace_id, query_data=query_data)

    df_col_names = []

    column_name_list = data['tables'][0]['columns']
    row_list = data['tables'][0]['rows']

    for item in column_name_list:
        df_col_names.append(item['name'])

    df_output = pd.DataFrame(row_list, columns=df_col_names)

    return df_output


def sentinel_mgt_oath_token(*, tenant_id, client_id, client_secret):
    auth_resp = soc.aztools.oauth_arm(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    auth_token = soc.aztools.oauth_bearer_token(auth_resp)
    return auth_token


def sentinel_list_logic(*, bearer_token, sub_id, resource_groupname, workspace_name, api='2023-02-01'):
    # '2023-02-01' API is the latest stable release so default to that if no arg is input
    api_call_url = f'https://management.azure.com/subscriptions/{sub_id}/resourceGroups/{resource_groupname}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/providers/Microsoft.SecurityInsights/alertRules?api-version={api}'

    req_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + bearer_token
    }

    api_call_response = requests.request('GET', api_call_url, headers=req_headers).json()
    json_object = json.dumps(api_call_response)
    return json_object


def sentinel_list_logic_flat_df(*, bearer_token, sub_id, resource_groupname, workspace_name, api='2023-02-01'):

    jsonobj = sentinel_list_logic(bearer_token=bearer_token,
                                  sub_id=sub_id,
                                  resource_groupname=resource_groupname,
                                  workspace_name=workspace_name,
                                  api=api)

    raw_df = pd.read_json(jsonobj, orient='columns')

    raw_df = pd.concat([raw_df, raw_df['value'].apply(pd.Series)], axis=1)
    raw_df = raw_df.drop('value', axis=1)
    raw_df = pd.concat([raw_df, raw_df['properties'].apply(pd.Series)], axis=1)
    raw_df = raw_df.drop('properties', axis=1)
    raw_df = pd.concat([raw_df, raw_df['eventGroupingSettings'].apply(pd.Series)], axis=1)
    raw_df = raw_df.drop('eventGroupingSettings', axis=1)
    raw_df = pd.concat([raw_df, raw_df['incidentConfiguration'].apply(pd.Series)], axis=1)
    raw_df = raw_df.drop('incidentConfiguration', axis=1)
    raw_df = pd.concat([raw_df, raw_df['groupingConfiguration'].apply(pd.Series)], axis=1)
    raw_df = raw_df.drop('groupingConfiguration', axis=1)

    meta_df = raw_df

    meta_df['dumpDateUtc'] = datetime.utcnow()
    col_a = meta_df.pop('lastModifiedUtc')
    col_b = meta_df.pop('dumpDateUtc')
    col_c = meta_df.pop('displayName')

    meta_df.insert(0, col_a.name, col_a)
    meta_df.insert(1, col_b.name, col_b)
    meta_df.insert(2, col_c.name, col_c)

    return meta_df.sort_values(by=['lastModifiedUtc'], ascending=False)

