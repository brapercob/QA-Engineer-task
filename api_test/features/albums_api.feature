Feature: Albums API no auth
  As a user,
  I want to get the list of albums,
  So they match with the ones expected

  Scenario: Verify first 5 albums on the response without authentication are as expected
    Given I made the request to the API
    Then I should get the response
    And The albums match with the expected


  #Background: User has authorization code
   # Given I have authorization code

  #Scenario: Verify first 5 albums on the response with authorization code are as expected
   # When I get the list of albums with code
    #Then I should get the response
    #And The albums match with the expected
