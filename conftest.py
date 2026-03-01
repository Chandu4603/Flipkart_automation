import pytest

@pytest.fixture
def start():
    import time
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(r'https://www.flipkart.com/')
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.close()