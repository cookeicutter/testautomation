from selenium import webdriver
import HomePage
import PageOperations
from behave import given, when, then

driver = webdriver.Firefox()

#homePage = HomePage(driver)
#pageOperations = PageOperations(driver)

@given("The user name is {string}")
def the_user_name_is(string):
    HomePage.loginOpen()
    HomePage.loginUserName(string)

@given("The password is {string}")
def the_password_is(string):
    HomePage.loginPassword(string)

@when("The green login button clicked")
def the_green_login_button_clicked():
    HomePage.loginClick()

@then("Login should be not success")
def login_should_be_not_success():
    assert PageOperations.findElementByClassName("error-message-container").is_displayed()
    HomePage.quitDriver()
    driver.quit()