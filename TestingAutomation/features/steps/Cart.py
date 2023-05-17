from selenium import webdriver
from HomePage import *
from HomePage import HomePage
from Purchase import *
from PageOperations import *
import time
from behave import *

    
  
       

@given("Open the site and login")
def open_the_site_and_login(context):
    context.driver = webdriver.Firefox()
    homePage = HomePage(context.driver)
    homePage.login()

@when("Add product to cart with {string} button")
def add_product_to_cart_with_button(context, string):
    pageOperations = PageOperations(context.driver)
    pageOperations.find_element_by_id_and_click(string)

@when("Open the cart")
def open_the_cart(context):
    pageOperations = PageOperations(context.driver)
    pageOperations.open_url("https://www.saucedemo.com/cart.html")

@then("Remove the product from the cart with {string} button")
def remove_the_product_from_the_cart_with_button(context, string):
    homePage = HomePage(context.driver)
    pageOperations = PageOperations(context.driver)
    pageOperations.find_element_by_id_and_click(string)
    time.sleep(2)
    homePage.quit_driver()
