import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from behave import given, when, then
import HomePage
import PageOperations

driver = webdriver.Firefox(service=Service())
#homePage = HomePage(driver)
#pageOperations = PageOperations(driver)

@given("The user sign in to the site")
def the_user_sign_in_to_the_site():
    HomePage.login()

@when("The about button clicked")
def the_about_button_clicked():
    PageOperations.findElementByIdAndClick("react-burger-menu-btn")
    PageOperations.findElementByIdAndClick("about_sidebar_link")

@then("Redirection should be success")
def redirection_should_be_success():
    time.sleep(2)
    assert driver.current_url == "https://saucelabs.com/"
    HomePage.quitDriver()