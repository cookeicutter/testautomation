Feature: Logout test
  Scenario: Logout should be success
    Given Open the homepage
    And Login to the site
    When The logout button clicked
    Then Logout should be success