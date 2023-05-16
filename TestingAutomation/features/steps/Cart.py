from selenium import webdriver
from HomePage import *
from PageOperations import *
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from behave import *


class Cart:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.options = Options()
        #options.headless = True
        homePage = HomePage(driver)
        pageOperations = PageOperations(driver)

        @given('Open the site and login')
        def open_the_site_and_login(self):
            homePage.login()

        @when("Add product to cart with {string} button")
        def add_product_to_cart_with_button(self, string):
            pageOperations.find_element_by_id_and_click(string)

        @when("Open the cart")
        def open_the_cart(self):
            pageOperations.open_url("https://www.saucedemo.com/cart.html")

        @then("Remove the product from the cart with {string} button")
        def remove_the_product_from_the_cart_with_button(self, string):
            pageOperations.find_element_by_id_and_click(string)
            time.sleep(2)
            homePage.quit_driver()
