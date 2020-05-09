# coding = utf-8
import pytest
import xlrd
from selenium import webdriver
from time import sleep, ctime
import os
from .const import *


class Test_baidu_search():
    def test_search_from_excel(self, excel_dir=EXCEL_DIR):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        excel_file = xlrd.open_workbook(EXCEL_DIR)
        sheet = excel_file.sheet_by_index(0)
        cols = sheet.col_values(0)
        #print(cols)
        for query in cols:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(query))
            driver.find_element_by_id("su").click()
            sleep(2)

        driver.quit()

    def test_ssss(self):
        print("111111111111111")
        assert 1==1

    def test_fail(self):
        print("222222222222222")
        assert 1==10
