#JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ

from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import *



@given("The user name is standard_user")
def the_user_name_is_standard_user(context):
    context.driver = webdriver.Firefox()
    homePage = HomePage(context.driver)
    homePage.login_open()
    homePage.login_user_name("standard_user")

    

@given("The password is secret_sauce")
def the_password_is_secret_sauce(context):
    homePage = HomePage(context.driver)
    homePage.login_password("secret_sauce")

@when("The login button clicked")
def the_login_button_clicked(context):
    homePage = HomePage(context.driver)
    homePage.login_click()

@then("Login should be success")
def login_should_be_success(context):
    pageOperations = PageOperations(context.driver)
    homePage = HomePage(context.driver)
    assert "inventory" in pageOperations.get_current_url()
    homePage.quit_driver()
    