Feature: Albums API with credentials
  As a user with credentials,
  I want to get the list of albums,
  So they match with the ones expected

  Background: User has client credentials
    Given I have client credentials

  Scenario: Verify first 5 albums on the response with client credentials are as expected
    When I make the request to the API with credentials
    Then I should get the response
    And The albums match with the expected