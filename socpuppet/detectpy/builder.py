import os
import socpuppet.aztools as az
import pandas as pd


def detectpy_path():
    """
    Gets absolute path of detectpy module

    :return: absolute path of detectpy module
    """
    dpath = os.path.dirname(os.path.abspath(__file__))

    return dpath


def mde_query_builder(data, lookback):
    """
    Extracts and Builds KQL Query from yaml config

    :param data: JSON Import of Logic_MDE Yaml
    :param lookback: Lookback Time for query
    :return: Dict Object of Key Value Pair {'query' : "query"} for MDE Advanced Hunting API Calls
    """

    detect = data.get('detect')
    title = detect.get('title')
    kql = data.get('logic')
    kql_var = kql.get('kqlVar')
    kql_table = kql.get('kqlTable')
    kql_query = kql.get('kqlQuery')

    if kql_var is not None:
        logic = kql_var + kql_table + f' | where Timestamp >= ago({lookback})' + kql_query
    else:
        logic = kql_table + f' | where Timestamp >= ago({lookback})' + kql_query

    output = {'title': title,
              'query': logic
              }

    return output


def mde_query_runner(*, bearer_token, query):
    """
    Runs query against M365D

    :param bearer_token: Azure Bearer Token
    :param query:
    :return:
    """
    response = az.mde_run_hunting_query(token=bearer_token, query_data=query)

    if 'results' in response:
        df = az.mde_run_hunting_query_df(token=bearer_token, query_data=query)
        logic_series = pd.Series(str(query), index=df.index)
        df['Logic'] = logic_series

        output = df

    else:
        output = response

    return output


def azmon_query_builder(data, lookback):
    """
    Extracts and Builds KQL Query from yaml config

    :param data: JSON Import of logic_azmon Yaml
    :param lookback: Lookback Time for query
    :return: Dict Object of Key Value Pair {'query' : "query"} for MDE Advanced Hunting API Calls
    """
    title = data.get('title')
    kql = data.get('logic')
    kql_var = kql.get('kqlVar')
    kql_table = kql.get('kqlTable')
    kql_query = kql.get('kqlQuery')

    if kql_var is not None:
        logic = kql_var + kql_table + f' | where TimeGenerated >= ago({lookback})' + kql_query
    else:
        logic = kql_table + f' | where TimeGenerated >= ago({lookback})' + kql_query

    output = {'title': title,
              'query': logic
              }

    return output


def azmon_query_runner(*, bearer_token, workspace_id, query):
    """
    Runs Query against Azure Monitor/Sentinel

    :param bearer_token: Azure Bearer Token
    :param workspace_id: Workspace ID of Sentinel/Azure Monitor Instance
    :param query: KQL Query
    :return: Dataframe of Query Results or Response Output if an Error
    """
    response = az.azmonitor_run_query(token=bearer_token, workspace_id=workspace_id, query_data=query)

    if 'tables' in response:
        df = az.azmonitor_run_query_df(token=bearer_token, workspace_id=workspace_id, query_data=query)
        logic_series = pd.Series(str(query), index=df.index)
        df['Logic'] = logic_series

        output = df

    else:
        output = response

    return output

