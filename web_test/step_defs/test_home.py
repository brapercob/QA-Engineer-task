from pytest_bdd import scenarios, then, parsers

from web_test.pages.base import BasePage

scenarios('../features/bcnc_home.feature')


# Check paragraphs are not empty
@then(parsers.parse('paragraphs are present and have content'))
def verify_paragraphs(driver):
    paragraphs = BasePage(driver).get_paragraphs()
    all_content = all(p.text for p in paragraphs)
    assert all_content and len(paragraphs) == 5
