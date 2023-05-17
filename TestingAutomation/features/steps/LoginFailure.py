#JÓÓÓÓÓÓÓÓÓÓÓ?????????????????
from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import *



@given("The user name is {string}")
def the_user_name_is(context, string):
    context.driver = webdriver.Firefox()
    homePage = HomePage(context.driver)
    homePage.login_open()
    homePage.login_user_name(string)

@given("The password is {string}")
def the_password_is(context, string):
    homePage = HomePage(context.driver)
    homePage.login_password(string)

@when("The green login button clicked")
def the_green_login_button_clicked(context):
    homePage = HomePage(context.driver)
    homePage.login_click()

@then("Login should be not success")
def login_should_be_not_success(context):
    homePage = HomePage(context.driver)
    pageOperations = PageOperations(context.driver)
    assert pageOperations.find_element_by_class_name("error-message-container").is_displayed()
    homePage.quit_driver()
    