import msal
import requests
import exceptions
from config.setup import settings

config = {
    "client_id": settings.AZURE_B2C.CLIENT_ID,
    "client_secret": settings.AZURE_B2C.CLIENT_SECRET,
    "authority": settings.AZURE_B2C.AUTHORITY,
    "scope": [settings.AZURE_B2C.SCOPE],
}

client = msal.ConfidentialClientApplication(
    config["client_id"],
    authority=config["authority"],
    client_credential=config["client_secret"],
)


def __get_auth_header():
    token_result = client.acquire_token_silent(config["scope"], account=None)

    if not token_result:
        token_result = client.acquire_token_for_client(scopes=config["scope"])

    if "access_token" in token_result:
        token = token_result["access_token"]
        if token:
            return {"Authorization": "Bearer " + token}
    raise exceptions.token_b2c_exception


def __user_structure(user):

    return {
        "surname": user.last_name,
        "givenName": user.first_name,
        "displayName": user.first_name + " " + user.last_name,
        "passwordProfile": {
            "forceChangePasswordNextSignIn": False,
            "password": user.password,
        },
        "identities": [
            {
                "signInType": "emailAddress",
                "issuer": "imetrix.onmicrosoft.com",
                "issuerAssignedId": user.email,
            }
        ],
    }


def graph_create(user):
    url = settings.AZURE_B2C.BASE_URL_GRAPH

    headers = __get_auth_header()
    try:
        user = {
            **__user_structure(user),
            "passwordPolicies": "DisablePasswordExpiration",
        }
        response = requests.post(url=url, headers=headers, json=user).json()
        return response["id"]

    except Exception:
        raise exceptions.b2c_create_exception


def graph_update(id, user):
    url = f"{settings.AZURE_B2C.BASE_URL_GRAPH}/{id}"
    headers = __get_auth_header()
    try:
        enabled = False
        if user.state == 1:
            enabled = True
        update_user = {"accountEnabled": enabled, **__user_structure(user)}
        requests.patch(url=url, headers=headers, json=update_user)
        

    except Exception:
        raise exceptions.b2c_update_exception
