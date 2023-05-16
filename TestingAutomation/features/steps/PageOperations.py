from typing import List
from selenium.webdriver import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class PageOperations:
    def __init__(self, driver: webdriver):
        self.driver = driver

       
    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element_by_id(self, element):
        return self.driver.find_element_by_id(element)

    def find_element_by_id_and_click(self, element):
        self.driver.find_element_by_id(element).click()

    def find_element_by_class_name(self, element):
        return self.driver.find_element_by_class_name(element)

    def find_elements_by_class_name_list(self, element):
        return self.driver.find_elements_by_class_name(element)

    def find_element_by_class_name_and_click(self, element):
        self.driver.find_element_by_class_name(element).click()

    def find_element_by_tag_name_and_click(self, element):
        self.driver.find_element_by_tag_name(element).click()

