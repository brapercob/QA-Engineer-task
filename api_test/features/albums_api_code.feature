Feature: Albums API with authorization code
  As a user with authorization code,
  I want to get the list of albums,
  So they match with the ones expected

  Background: User has authorization code
    Given I have authorization code

  Scenario: Verify first 5 albums on the response with authorization code are as expected
    When I make the request to the API with code
    Then I should get the response
    And The albums match with the expected