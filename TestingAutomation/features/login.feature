Feature: Login test
  Scenario: Login should be success
    Given The user name is standard_user
    And The password is secret_sauce
    When The login button clicked
    Then Login should be success