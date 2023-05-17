#JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from behave import given, when, then
from HomePage import *
from PageOperations import *




@given("The user sign in to the site")
def the_user_sign_in_to_the_site(context):
    context.driver = webdriver.Firefox()
    homePage = HomePage(context.driver) 
    homePage.login()

@when("The about button clicked")
def the_about_button_clicked(context):
    
    pageOperations = PageOperations(context.driver)
    pageOperations.find_element_by_id_and_click("react-burger-menu-btn")
    pageOperations.find_element_by_id_and_click("about_sidebar_link")
   

@then("Redirection should be success")
def redirection_should_be_success(context):
    homePage = HomePage(context.driver)
    time.sleep(2)
    teszt = context.driver.current_url
     
    assert ( teszt == "https://saucelabs.com/")
    homePage.quit_driver()