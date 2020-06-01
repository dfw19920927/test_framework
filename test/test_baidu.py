import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader


class testBaidu(unittest.TestCase):
    # URL = 'http://www.baidu.com'
    # base_path = os.path.dirname(os.path.abspath(__file__))+'\..'
    # driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
    #     self.driver.get(self.URL)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

    # def test_search_0(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)
    #
    # def test_search_1(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('python selenium')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)