

from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import given, when, then

driver = webdriver.Firefox()

homePage = HomePage(driver)
pageOperations = PageOperations(driver)

@given("Open the homepage")
def open_the_homepage(this):
    homePage.login_open
    

@given("Login to the site")
def login_to_the_site(this):
    time.sleep(3)
    homePage.login_user_name( "standard_user")
    homePage.login_password( "secret_sauce")
    homePage.login_click()

@when("The logout button clicked")
def the_logout_button_clicked(this):
    pageOperations.find_element_by_id_and_click("react-burger-menu-btn")
    pageOperations.find_element_by_id_and_click("logout_sidebar_link")

@then("Logout should be success")
def logout_should_be_success(this):
    assert pageOperations.get_current_url() == "https://www.saucedemo.com/"
    homePage.quit_driver()
    driver.quit()