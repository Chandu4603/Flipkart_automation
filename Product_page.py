from selenium.webdriver.common.by import By


class PRODUCT:
    add_to_cart="//button[@class='QqFHMw vslbG+ In9uk2']"
    buy_now="//button[@type='button']"

    def __init__(self,driver):
        self.driver=driver

    def cart(self):
        self.driver.find_element(By.XPATH,self.add_to_cart).click()

    def buy(self):
        self.driver.find_element(By.XPATH,self.buy_now).click()