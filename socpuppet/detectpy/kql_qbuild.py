

def kql_single_table_query_builder(data, time_period):
    logic = data.get('kqlTable') + f'| where Timestamp >= ago({time_period})' + data.get('kqlQuery')
    output = {'query': logic}
    return output

