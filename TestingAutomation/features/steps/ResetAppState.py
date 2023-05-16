import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from HomePage import *
from PageOperations import *


class ResetAppState:
    def __init__(self):
        self.driver10 = webdriver.Firefox()
        self.homePage10 = HomePage(self.driver10)
        self.pageOperations10 = PageOperations(self.driver10)

    @given("The user logs in to the site")
    def the_user_logs_in_to_the_site(self):
        self.homePage10.login()

    @given("Add {string} and {string} to the cart")
    def add_and_to_the_cart(self, string1, string2):
        self.pageOperations10.find_element_by_id_and_click(string1)
        self.pageOperations10.find_element_by_id_and_click(string2)

    @when("The reset app state button is clicked")
    def the_reset_app_state_button_is_clicked(self):
        self.pageOperations10.find_element_by_id_and_click("react-burger-menu-btn")
        self.pageOperations10.find_element_by_id_and_click("reset_sidebar_link")

    @then("Cart is empty")
    def cart_is_empty(self):        
        assert ("0" in self.pageOperations10.find_element_by_class_name("shopping_cart_badge"))
        self.homePage10.quit_driver()
