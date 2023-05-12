import requests

from pytest_bdd import scenarios, given, then

scenarios('../albums_api.feature')


API = 'https://jsonplaceholder.typicode.com/albums'


@given('I made the request to the API', target_fixture='response')
def get_response_request():
    response = requests.get(API)
    return response


@then('I should get the response')
def get_response_code(response):
    assert response.status_code == 200


@then('The albums match with the expected')
def get_match(get_albums, response):

    albums = response.json()
    titles = []
    for i in range(5):
        titles.append(albums[i].get('title'))
    assert titles == get_albums





