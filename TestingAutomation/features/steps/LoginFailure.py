from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import given, when, then

driver = webdriver.Firefox()

homePage = HomePage(driver)
pageOperations = PageOperations(driver)

@given("The user name is {string}")
def the_user_name_is(this, string):
    homePage.login_open()
    homePage.login_user_name(string)

@given("The password is {string}")
def the_password_is(this, string):
    homePage.login_password(string)

@when("The green login button clicked")
def the_green_login_button_clicked(this):
    homePage.login_click()

@then("Login should be not success")
def login_should_be_not_success(this):
    assert pageOperations.find_element_by_class_name("error-message-container").is_displayed()
    homePage.quit_driver()
    driver.quit()