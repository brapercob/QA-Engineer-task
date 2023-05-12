Feature: BCNC Home page
  As a user,
  I want to get the paragraphs from the home page,
  So the content on them are checked correct.

  Background: Navigate to BCNC HOME page
    Given I have navigated to 'BCNC' "Home" page

  Scenario: Verify paragraphs are present on HOME section
    Then paragraphs are present and have content
