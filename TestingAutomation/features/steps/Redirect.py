#JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from behave import given, when, then
from HomePage import *
from PageOperations import *


driver1 = webdriver.Firefox()
homePage = HomePage(driver1)
pageOperations = PageOperations(driver1)

@given("The user sign in to the site")
def the_user_sign_in_to_the_site(this):
    homePage.login()

@when("The about button clicked")
def the_about_button_clicked(this):
    pageOperations.find_element_by_id_and_click("react-burger-menu-btn")
    pageOperations.find_element_by_id_and_click("about_sidebar_link")

@then("Redirection should be success")
def redirection_should_be_success(this):
    time.sleep(2)
    teszt = driver1.current_url
     
    assert ( teszt == "https://saucelabs.com/")
    homePage.quit_driver()