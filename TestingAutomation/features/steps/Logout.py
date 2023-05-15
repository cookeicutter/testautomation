

from selenium import webdriver
import HomePage
import PageOperations
from behave import given, when, then

driver = webdriver.Firefox()

#homePage = HomePage(driver)
#pageOperations = PageOperations(driver)

@given("Open the homepage")
def open_the_homepage():
    HomePage.loginOpen()

@given("Login to the site")
def login_to_the_site():
    HomePage.loginUserName("standard_user")
    HomePage.loginPassword("secret_sauce")
    HomePage.loginClick()

@when("The logout button clicked")
def the_logout_button_clicked():
    PageOperations.findElementByIdAndClick("react-burger-menu-btn")
    PageOperations.findElementByIdAndClick("logout_sidebar_link")

@then("Logout should be success")
def logout_should_be_success():
    assert PageOperations.getCurrentUrl() == "https://www.saucedemo.com/"
    HomePage.quitDriver()
    driver.quit()