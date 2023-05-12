Feature: BCNC Who we are page
  As a user,
  I want to get the paragraphs from the who we are page,
  So the content on them are checked correct.

  Background: Navigate to BCNC Who we are page
    Given I have navigated to 'BCNC' "Who we are" page

  Scenario: Verify paragraphs are present on WHO WE ARE section
    Then paragraphs are present and have content
