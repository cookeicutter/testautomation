from selenium import webdriver
from HomePage import *
from HomePage import HomePage
from Purchase import *
from PageOperations import *
import time
from behave import *

    
driver1 = webdriver.Firefox()
homePage1 = HomePage(driver1)
pageOperations1 = PageOperations(driver1)         
       

@given("Open the site and login")
def open_the_site_and_login(this):
    homePage1.login()

@when("Add product to cart with {string} button")
def add_product_to_cart_with_button(this, string):
    pageOperations1.find_element_by_id_and_click(string)

@when("Open the cart")
def open_the_cart(this):
    pageOperations1.open_url("https://www.saucedemo.com/cart.html")

@then("Remove the product from the cart with {string} button")
def remove_the_product_from_the_cart_with_button(this, string):
    pageOperations1.find_element_by_id_and_click(string)
    time.sleep(2)
    driver1.quit()
