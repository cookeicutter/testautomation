from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.NAME, "login-button").click()

    def login_open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_user_name(self, username):
        self.driver.find_element(By.NAME, "user-name").send_keys(username)

    def login_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def login_click(self):
        self.driver.find_element(By.NAME, "login-button").click()

    def quit_driver(self):
        self.driver.quit()
