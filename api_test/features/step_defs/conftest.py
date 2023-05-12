import pytest
import openpyxl
import os
from pytest_bdd import then


@pytest.fixture
def get_albums():
    albums = []
    book = openpyxl.load_workbook(os.path.abspath('album_data/albums.xlsx'))
    sheet = book['Hoja1']
    for c in sheet['A'][0:5]:
        albums.append(c.value)
    return albums


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

