import requests

from pytest_bdd import scenarios, given, when

scenarios('../albums_api_code.feature')

API = 'https://jsonplaceholder.typicode.com/albums'


@given("I have authorization code", target_fixture='token')
def get_credentials():
    token_url = 'https://jsonplaceholder.typicode.com/oauth/token'
    client_id = 'example_client_id'
    client_secret = 'example_client_secret'

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(token_url, data=data)

    # Assert the response is 200
    # assert response.status_code == 200
    # Keep the token and make
    # access_token = response.json()["access_token"]
    access_token = 'example_token'
    return access_token


@when('I make the request to the API with code', target_fixture='response')
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
