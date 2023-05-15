Feature: Reset app state test
  Scenario Outline: Reset app state should be success
    Given The user logs in to the site
    And Add <item1> and <item2> to the cart
    When The reset app state button is clicked
    Then Cart is empty

    Examples:
    | item1 | item2 |
    | "add-to-cart-sauce-labs-backpack" | "add-to-cart-sauce-labs-bike-light" |
    | "add-to-cart-sauce-labs-bike-light" | "add-to-cart-sauce-labs-bolt-t-shirt" |
    | "add-to-cart-sauce-labs-bolt-t-shirt" | "add-to-cart-sauce-labs-fleece-jacket" |
    | "add-to-cart-sauce-labs-fleece-jacket" | "add-to-cart-sauce-labs-onesie" |
    | "add-to-cart-sauce-labs-onesie" | "add-to-cart-sauce-labs-backpack" |