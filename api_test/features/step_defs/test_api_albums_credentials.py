import requests

from pytest_bdd import scenarios, given, when

scenarios('../albums_api_credentials.feature')

API = 'https://jsonplaceholder.typicode.com/albums'


@given("I have client credentials", target_fixture='token')
def get_code_authorization():
    client_id = 'example_client_id'
    client_secret = 'example_client_secret'
    redirect_uri = 'https://exampledomain.com'
    authorize_url = 'https://jsonplaceholder.typicode.com/oauth/authorize'
    token_url = 'https://jsonplaceholder.typicode.com/oauth/token'
    scope = 'openid'

    # Get authorization page
    # requests.get('{}?response_type=code&client_id={}&redirect_url={}'
    #             .format(authorize_url, client_id, redirect_uri))

    # After this the user should have obtained the authorization code
    # It could be asked through the console input
    data = {
        'grant_type': 'authorization_code',
        'code': 'example_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_url': redirect_uri}
    # Make the post request with the code to get the token
    # token_response = requests.post(token_url, data=data)

    # Assert the response is 200
    # assert response.status_code == 200
    # Keep the token and make
    # access_token = response.json()["access_token"]
    access_token = 'example_token'
    return access_token


@when('I make the request to the API with credentials', target_fixture='response')
def get_response_request(token):
    # Define the headers for the request including the obtained token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    # Make the request including the headers with the token
    # response = requests.get("https://jsonplaceholder.typicode.com/albums", headers=headers)
    response = requests.get(API)
    assert response.status_code == 200
    return response
