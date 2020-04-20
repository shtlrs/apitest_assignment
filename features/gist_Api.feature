Feature: Github's gist API testing

  Scenario: Create new gist with valid json
     Given user creates a new gist with valid_json_body
      Then response code should be 201
      And the description of gist 1 should be correct


  Scenario: Create new gist with invalid json
      Given user creates a new gist with invalid_json_body
      Then response code should be 422


  Scenario: Create new gist with a string
      Given user creates a new gist with a_string
      Then response code should be 422


  Scenario: Create new gist with an integer
      Given user creates a new gist with an_int
      Then response code should be 422

  Scenario: Create new gist with a boolean
      Given user creates a new gist with a_boolean
      Then response code should be 422

  Scenario: Create new gist with a list
      Given user creates a new gist with a_list
      Then response code should be 422


  Scenario: Create new gist with invalid token
     Given user authenticates with invalid_token
      Then response code should be 401

  Scenario: Create new gist with no token
     Given user authenticates with no_token
      Then response code should be 401


  Scenario: Retrieve an existing gist by id
    Given user searches for an existing gist by id
    Then response code should be 200
    And the description of gist 2 should be correct

#
  Scenario: Retrieve an unexisting gist by id
    Given user searches for an unexisting gist by id
    Then response code should be 404
#
#
  Scenario: Update an existing gist
    Given user updates an existing gist by id
    Then response code should be 200
    And the description of gist 5 should be correct
#
#
  Scenario: Update an unexisting gist
    Given user updates an unexisting gist by id
    Then response code should be 404
#
#
  Scenario: Delete an existing gist
    Given user deletes an existing gist by id
    Then response code should be 204
#
  Scenario: Delete an unexisting gist
    Given user deletes an unexisting gist by id
    Then response code should be 404


