Feature: Cart test
  Scenario Outline: Adding and removing products to cart should be success
    Given Open the site and login
    When Add product to cart with <add-to-cart> button
    And Open the cart
    Then Remove the product from the cart with <remove-from-cart> button

    Examples:
      | add-to-cart | remove-from-cart |
      | add-to-cart-sauce-labs-backpack | remove-sauce-labs-backpack |
      | add-to-cart-sauce-labs-bike-light | remove-sauce-labs-bike-light |
      | add-to-cart-sauce-labs-bolt-t-shirt | remove-sauce-labs-bolt-t-shirt |
      | add-to-cart-sauce-labs-fleece-jacket | remove-sauce-labs-fleece-jacket |
      | add-to-cart-sauce-labs-onesie | remove-sauce-labs-onesie |