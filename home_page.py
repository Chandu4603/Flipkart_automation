from selenium.webdriver.common.by import By


class HOME:
    search_bar="//input[@placeholder='Search for Products, Brands and More']"
    Search_button="//*[name()='path' and contains(@d,'M10.5 18C1')]"
    product="//a[@class='VJA3rP']//img[@alt='Apple AirPods Pro (2nd generation) with MagSafe Case (USB-C) Bluetooth Headset']"

    def __init__(self,driver):
        self.driver=driver

    def Search(self,data):
        self.driver.find_element(By.XPATH,self.search_bar).send_keys(data)

    def Button(self):
        self.driver.find_element(By.XPATH,self.Search_button).submit()

    def Prod(self):
        self.driver.find_element(By.XPATH,self.product).click()