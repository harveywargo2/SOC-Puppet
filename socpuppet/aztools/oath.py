import requests


def oauth_graph(tenant_id: str, client_id: str, client_secret: str):
    auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

    resource_url = 'https://graph.microsoft.com'

    auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()

    return auth_response


def oauth_m365d_mde(tenant_id: str, client_id: str, client_secret: str):
    auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

    resource_url = 'https://api.securitycenter.windows.com'

    auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()

    return auth_response


def oauth_m365d_mtp(tenant_id: str, client_id: str, client_secret: str):
    auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

    resource_url = 'https://security.microsoft.com/mtp/'

    auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()

    return auth_response


def oauth_azure_monitor(tenant_id: str, client_id: str, client_secret: str):
    auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

    resource_url = 'https://api.loganalytics.io'

    auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()

    return auth_response


def oauth_arm(tenant_id: str, client_id: str, client_secret: str):
    auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

    resource_url = 'https://management.azure.com'

    auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()

    return auth_response


def oauth_bearer_token(auth_response: str):
    auth_token = auth_response['access_token']
    return auth_token

