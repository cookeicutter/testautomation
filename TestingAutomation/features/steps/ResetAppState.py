import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from behave import given, when, then
from HomePage import *
from PageOperations import *

driver = webdriver.Firefox(service=Service())
homePage = HomePage(driver)
pageOperations = PageOperations(driver)


class ResetAppState:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(executable_path='geckodriver'))
        self.homePage = HomePage(self.driver)
        self.pageOperations = PageOperations(self.driver)

    @given("The user logs in to the site")
    def the_user_logs_in_to_the_site(self):
        self.homePage.login()

    @given("Add {string} and {string} to the cart")
    def add_and_to_the_cart(self, string, string2):
        self.pageOperations.find_element_by_id_and_click(string)
        self.pageOperations.find_element_by_id_and_click(string2)

    @when("The reset app state button is clicked")
    def the_reset_app_state_button_is_clicked(self):
        self.pageOperations.find_element_by_id_and_click("react-burger-menu-btn")
        self.pageOperations.find_element_by_id_and_click("reset_sidebar_link")

    @then("Cart is empty")
    def cart_is_empty(self):
        
        assert "0" in self.pageOperations.find_element_by_class_name("shopping_cart_badge")
        self.homePage.quit_driver()
