Feature: Inventory sort test
  Scenario Outline: Product sorting should be success
    Given Open the inventory
    When The value of product sort container is <value>
    Then The products should be sorted

    Examples:
    | value |
    | "az" |
    | "za" |
    | "lohi" |
    | "hilo" |