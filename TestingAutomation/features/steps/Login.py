from selenium import webdriver
import HomePage
import PageOperations
from behave import given, when, then

driver = webdriver.Firefox()

#homePage = HomePage(driver)
#pageOperations = PageOperations(driver)

@given("The user name is standard_user")
def the_user_name_is_standard_user():
    HomePage.loginOpen()
    HomePage.loginUserName("standard_user")

@given("The password is secret_sauce")
def the_password_is_secret_sauce():
    HomePage.loginPassword("secret_sauce")

@when("The login button clicked")
def the_login_button_clicked():
    HomePage.loginClick()

@then("Login should be success")
def login_should_be_success():
    assert "inventory" in PageOperations.getCurrentUrl()
    HomePage.quitDriver()
    driver.quit()