Feature: Purchase item test
  Scenario Outline: Purchase item should be success
    Given Sign in to the site
    And Open the details page of the item with <button> button
    And Add the item to cart
    And Open the cart page
    And Open the checkout page
    And Fill the necessary fields with <firstName>, <lastName> and <postalCode>
    When The finish button clicked
    Then Purchase should be success

    Examples:
    | button | firstName | lastName | postalCode |
    | "add-to-cart-sauce-labs-backpack" | "John" | "Smith" | "1234" |
    | "add-to-cart-sauce-labs-bike-light" | "Agnes" | "Nichols" | "2345" |
    | "add-to-cart-sauce-labs-onesie" | "Jack" | "Johnson" | "5678" |
    | "add-to-cart-sauce-labs-fleece-jacket" | "Claire" | "Jefferson" | "9856" |