#JÓÓÓÓÓÓÓÓÓÓÓ?????????????????
from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import *



@given("The user name is {string}")
def the_user_name_is(context, string):
    context.driver = webdriver.Firefox()
    context.homePage = HomePage(context.driver)
    context.homePage.login_open()
    context.homePage.login_user_name(string)

@given("The password is {string}")
def the_password_is(context, string):
    context.homePage = HomePage(context.driver)
    context.homePage.login_password(string)

@when("The green login button clicked")
def the_green_login_button_clicked(context):
    context.homePage = HomePage(context.driver)
    context.homePage.login_click()

@then("Login should be not success")
def login_should_be_not_success(context):
    context.homePage = HomePage(context.driver)
    context.pageOperations = PageOperations(context.driver)
    assert context.pageOperations.find_element_by_class_name("error-message-container").is_displayed()
    context.homePage.quit_driver()
    