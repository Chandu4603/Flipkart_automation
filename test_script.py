import time

from Home_page import *
from Product_page import *

def test(start):
    driver=start

    H=HOME(driver)
    H.Search('earbuds')
    H.Button()
    H.Prod()

    wids=driver.window_handles
    h=wids[0]
    p=wids[1]
    driver.switch_to.window(p)

    P=PRODUCT(driver)
    P.buy()
    time.sleep(3)