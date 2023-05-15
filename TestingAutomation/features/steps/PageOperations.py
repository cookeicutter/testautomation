from typing import List

from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PageOperations:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def find_element_by_id(self, element_id: str) -> WebElement:
        return self.driver.find_element(By.ID, element_id)

    def find_element_by_id_and_click(self, element_id: str):
        self.driver.find_element(By.ID, element_id).click()

    def find_element_by_class_name(self, class_name: str) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def find_elements_by_class_name_list(self, class_name: str) -> List[WebElement]:
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_element_by_class_name_and_click(self, class_name: str):
        self.driver.find_element(By.CLASS_NAME, class_name).click()

    def find_element_by_tag_name_and_click(self, tag_name: str):
        self.driver.find_element(By.TAG_NAME, tag_name).click()
