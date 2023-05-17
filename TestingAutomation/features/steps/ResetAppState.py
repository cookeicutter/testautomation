from selenium import webdriver
from behave import *
from HomePage import *
from PageOperations import *
 
    

@given('The user logs in to the site')
def the_user_logs_in_to_the_site(context):
    context.driver = webdriver.Firefox()
    homePage = HomePage(context.driver)
    homePage.login()

@given('Add {string} and {string2} to the cart')
def add_and_to_the_cart(context, string, string2):
    pageOperations = PageOperations(context.driver)
    pageOperations.find_element_by_id_and_click(string)
    pageOperations.find_element_by_id_and_click(string2)
    


@when('The reset app state button is clicked')
def the_reset_app_state_button_is_clicked(context):
    pageOperations = PageOperations(context.driver)
    pageOperations.find_element_by_id_and_click('react-burger-menu-btn')
    pageOperations.find_element_by_id_and_click('reset_sidebar_link')

@then('Cart is empty')
def cart_is_empty(context): 
    pageOperations = PageOperations(context.driver)
    homePage = HomePage(context.driver)
        
    
    assert pageOperations.check_exists_by_classname('shopping_cart_badge') == False
    homePage.quit_driver()
