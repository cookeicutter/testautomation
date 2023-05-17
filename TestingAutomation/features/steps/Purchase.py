from selenium import webdriver
from HomePage import *
from PageOperations import *
from behave import *




class Purchase():
    def __init__(self, driver: webdriver):        
        self.driver = driver
        self.homePage = HomePage(self.driver)
        self.pageOperations = PageOperations(self.driver)

    @given("Sign in to the site")
    def sign_in_to_the_site(self):
        self.homePage.login()

    @given("Open the details page of the item with {string} button")
    def open_the_details_page_of_the_item_with_button(self, string):
        self.pageOperations.find_element_by_id_and_click(string)

    @given("Add the item to cart")
    def add_the_item_to_cart(self):
        self.pageOperations.find_element_by_tag_name_and_click("button")

    @given("Open the cart page")
    def open_the_cart_page(self):
        self.pageOperations.open_url("https://www.saucedemo.com/cart.html")

    @given("Open the checkout page")
    def open_the_checkout_page(self):
        self.pageOperations.find_element_by_id_and_click("checkout")

    @given("Fill the necessary fields with {string}, {string} and {string}")
    def fill_the_necessary_fields_with_and(self, string1, string2, string3):
        self.pageOperations.find_element_by_id("first-name").send_keys(string1)
        self.pageOperations.find_element_by_id("last-name").send_keys(string2)
        self.pageOperations.find_element_by_id("postal-code").send_keys(string3)
        self.pageOperations.find_element_by_id_and_click("continue")

    @when("The finish button clicked")
    def the_finish_button_clicked(self):
        self.pageOperations.find_element_by_id_and_click("finish")

    @then("Purchase should be success")
    def purchase_should_be_success(self):
        assert (self.pageOperations.find_element_by_class_name("complete-header").is_displayed())
        self.homePage.quit_driver()

