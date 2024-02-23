

def kql_single_table_builder(data, time_period, time_field):
    kql = data.get('kqlDetect')
    kql_var = kql.get('kqlVar')
    kql_table = kql.get('kqlTable')
    kql_query = kql.get('kqlQuery')

    if kql_var is not None:
        logic = kql_var + kql_table + f' | where {time_field} >= ago({time_period})' + kql_query
    else:
        logic = kql_table + f' | where {time_field} >= ago({time_period})' + kql_query

    output = {'query': logic}

    return output

