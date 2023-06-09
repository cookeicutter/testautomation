#JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ!!!!!!!!!!

from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import *



@given("Open the homepage")
def open_the_homepage(context):
    context.driver = webdriver.Firefox()
    context.homePage = HomePage(context.driver)
    context.homePage.login_open()
    

@given("Login to the site")
def login_to_the_site(context):
    context.homePage = HomePage(context.driver)
    time.sleep(3)
    context.homePage.login_user_name( "standard_user")
    context.homePage.login_password( "secret_sauce")
    context.homePage.login_click()

@when("The logout button clicked")
def the_logout_button_clicked(context):
    
    context.pageOperations = PageOperations(context.driver)
    context.pageOperations.find_element_by_id_and_click("react-burger-menu-btn")
    context.pageOperations.find_element_by_id_and_click("logout_sidebar_link")

@then("Logout should be success")
def logout_should_be_success(context):
    
    context.homePage = HomePage(context.driver)
    context.pageOperations = PageOperations(context.driver)
    assert context.pageOperations.get_current_url() == "https://www.saucedemo.com/"
    context.homePage.quit_driver()
    