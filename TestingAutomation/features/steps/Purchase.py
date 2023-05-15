from selenium import webdriver
import HomePage
import PageOperations
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import unittest
from behave import given, when, then

class Purchase(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path="path/to/geckodriver")
        self.driver = webdriver.Firefox(service=self.service)
        self.homePage = HomePage(self.driver)
        self.pageOperations = PageOperations(self.driver)

    @given("Sign in to the site")
    def sign_in_to_the_site(self):
        self.homePage.login()

    @given("Open the details page of the item with {string} button")
    def open_the_details_page_of_the_item_with_button(self, string):
        self.pageOperations.findElementByIdAndClick(string)

    @given("Add the item to cart")
    def add_the_item_to_cart(self):
        self.pageOperations.findElementByTagNameAndClick("button")

    @given("Open the cart page")
    def open_the_cart_page(self):
        self.pageOperations.openUrl("https://www.saucedemo.com/cart.html")

    @given("Open the checkout page")
    def open_the_checkout_page(self):
        self.pageOperations.findElementByIdAndClick("checkout")

    @given("Fill the necessary fields with {string}, {string} and {string}")
    def fill_the_necessary_fields_with_and(self, string, string2, string3):
        self.pageOperations.findElementById("first-name").send_keys(string)
        self.pageOperations.findElementById("last-name").send_keys(string2)
        self.pageOperations.findElementById("postal-code").send_keys(string3)
        self.pageOperations.findElementByIdAndClick("continue")

    @when("The finish button clicked")
    def the_finish_button_clicked(self):
        self.pageOperations.findElementByIdAndClick("finish")

    @then("Purchase should be success")
    def purchase_should_be_success(self):
        self.assertTrue(self.pageOperations.findElementByClassName("complete-header").is_displayed())
        self.homePage.quitDriver()

    def tearDown(self):
        self.driver.quit()
