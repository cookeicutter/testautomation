from selenium import webdriver
import HomePage
import PageOperations
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from behave import *


class Cart:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox()

    #homePage = HomePage(driver)
    #pageOperations = PageOperations(driver)

    @given('Open the site and login')
    def open_the_site_and_login(self):
        HomePage.login()

    @when("Add product to cart with {string} button")
    def add_product_to_cart_with_button(self, string):
        PageOperations.findElementByIdAndClick(string)

    @when("Open the cart")
    def open_the_cart(self):
       PageOperations.openUrl("https://www.saucedemo.com/cart.html")

    @then("Remove the product from the cart with {string} button")
    def remove_the_product_from_the_cart_with_button(self, string):
        PageOperations.findElementByIdAndClick(string)
        time.sleep(2)
        HomePage.quitDriver()
