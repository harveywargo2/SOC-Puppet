import requests
import socpuppet as soc
import pandas as pd
import json
from datetime import datetime


def mde_oath_token(*, tenant_id, client_id, client_secret):
    auth_resp = soc.aztools.oauth_graph(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    auth_token = soc.aztools.oauth_bearer_token(auth_resp)
    return auth_token


def mde_mgt_oauth_token(*, tenant_id: str, client_id: str, client_secret: str):
    auth_resp = soc.aztools.oauth_m365d_mtp(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    auth_token = soc.aztools.oauth_bearer_token(auth_resp)
    return auth_token


def mde_run_hunting_query(*, token, query_data):
    api_call_url = f'https://graph.microsoft.com/v1.0/security/runHuntingQuery'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    api_call_response = requests.request('POST', api_call_url, headers=headers, json=query_data).json()

    return api_call_response


def mde_run_hunting_query_df(*, token, query_data):
    output = mde_run_hunting_query(token=token, query_data=query_data)
    mde_df = pd.DataFrame.from_dict(output['results'])

    return mde_df


def mde_list_hunting_logic(*, token):
    """
    :param token: (string) bearer/auth token
    :return: (dict)
    """
    api_call_url = 'https://api.security.microsoft.com/api/CustomDetections'
    req_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
            }

    api_call_response = requests.request('GET', api_call_url, headers=req_headers).json()
    return json.dumps(api_call_response)


def mde_list_hunting_logic_flat_df(*, token):
    data = mde_list_hunting_logic(token=token)
    mde_df = pd.read_json(data)
    mde_df = pd.concat([mde_df, mde_df['value'].apply(pd.Series)], axis=1)
    mde_df = mde_df.drop('value', axis=1)

    mde_df['dumpDateUtc'] = datetime.utcnow()

    col_a = mde_df.pop('lastUpdatedTime')
    col_b = mde_df.pop('dumpDateUtc')
    col_c = mde_df.pop('ruleName')

    mde_df.insert(0, col_a.name, col_a)
    mde_df.insert(1, col_b.name, col_b)
    mde_df.insert(2, col_c.name, col_c)

    return mde_df

