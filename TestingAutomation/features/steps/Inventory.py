import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *
from HomePage import *
from PageOperations import *

class Inventory:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.homePage = HomePage(self.driver)
        self.pageOperations = PageOperations(self.driver)
    
    @given("Open the inventory")
    def open_the_inventory(self):
        self.homePage.login()


    @when("The value of product sort container is {string}")
    def the_value_of_product_sort_container_is(self, string):
        select = (self.pageOperations.find_element_by_class_name("product_sort_container"))
        select.select_by_value(string)
        self.testValue = string
    
    @then("The products should be sorted")
    def the_products_should_be_sorted(self):
        if self.testValue == "az":
            self.myList = self.pageOperations.find_elements_by_class_name_list("inventory_item_name")
            self.assertEqual(self.myList[0].text, "Sauce Labs Backpack")
        elif self.testValue == "za":
            self.myList = self.pageOperations.find_elements_by_class_name_list("inventory_item_name")
            self.assertEqual(self.myList[0].text, "Test.allTheThings() T-Shirt (Red)")
        elif self.testValue == "hilo":
            self.myList = self.pageOperations.find_elements_by_class_name_list("inventory_item_name")
            self.assertEqual(self.myList[0].text, "Sauce Labs Fleece Jacket")
        elif self.testValue == "lohi":
            self.myList = self.pageOperations.find_elements_by_class_name_list("inventory_item_name")
            self.assertEqual(self.myList[0].text, "Sauce Labs Onesie")

        self.homePage.quit_driver()