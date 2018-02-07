import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class SearchGoogle(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome('./chromedriver')

    def waitForElement(self,by,value):
        try:
            element = WebDriverWait(self.driver, 30).until(
                expected_conditions.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False
    def searchInGoogle(self):
        driver=self.driver
        driver.get("http://www.google.co.il")
        if (self.waitForElement(By.NAME,"q")):
            driver.find_element(By.NAME,"q").send_keys("python")
            driver.find_element(By.NAME,"q").submit()
            if (self.waitForElement(By.NAME,"q")):
              links=  driver.find_elements_by_css_selector("h3.r a")
              for link in links:
                 print(link.get_attribute("text"))




    def tearDown(self):
        self.driver.maximize_window()

    if __name__ == "__main__":
        unittest.main()
