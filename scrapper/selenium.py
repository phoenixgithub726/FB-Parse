from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from utils.setting import setting
from utils.log import log

_chrome = None
class chrome:

    @staticmethod
    def getInstance():
        global _chrome
        if _chrome == None:
            _chrome = chrome()
        return _chrome

    def __init__(self):
        chrome_driver_path = setting.getInstance().get('CHROMEDRIVER')
        self.driver = webdriver.Chrome(chrome_driver_path)

    def getHtml(self):
        return self.driver.page_source

    def doAction(self, message=None, action='', params={}):
        if message !=None:
            log.getInstance().printLog(message)
        
        # switch(actions) case action
        actions = {
            'open': self.open,
            'getValue': self.getValue,
            'setValue': self.setValue,
            'click': self.click,
            'wait_for_pageload': self.wait_for_pageload
        }
        func = actions.get(action)
        return func(params)

    def open(self, params):
        if params.get('url') != None:
            self.driver.get(params.get('url'))
            return True
        return False

    def wait_for_pageload(self, params):
        time.sleep(5)
        start_time = time.time()
        while time.time() < start_time + 5:
            if self.driver.execute_script('return document.readyState;') == 'complete' :
                return True
            else:
                time.sleep(0.1)
        return False

    def setValue(self, params={}):
        if params.get('name') != None:
            self.driver.find_element_by_name(params.get('name')).send_keys(params.get('value'))
            return True
        return False
    def getValue(self, params={}):
        return None

    def click(self, params={}):
        ele = None
        self.driver.find_element_by_css_selector(".login_form_login_button").click()
        # if params.get('tag') != None:
        #     for button in self.driver.find_elements_by_tag_name(params.get('tag')):
        #         if button.text == params.get('text'):
        #             ele = button
        #             break
        
        # if ele != None:
        #     ele.click()
        #     return True
        return False
