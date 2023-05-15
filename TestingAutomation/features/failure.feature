Feature: Login fail
  Scenario Outline: Login shouldn't be success
    Given The user name is <user>
    And The password is <pass>
    When The green login button clicked
    Then Login should be not success

    Examples:
    | user | pass |
    | "locked_out_user" | "secret_sauce" |
    | "TestUser1" | "TestPassword1" |
    | "TestUser2" | "TestPassword2" |
    | "TestUser3" | "TestPassword3" |
    | "TestUser4" | "TestPassword4" |