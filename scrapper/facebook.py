from bs4 import BeautifulSoup
from scrapper.selenium import chrome

from utils.log import log
from utils.setting import setting

_facebook = None
class FaceBook:
    @staticmethod
    def getInstance():
        global _facebook
        if _facebook == None:
            _facebook = FaceBook()
        return _facebook

    def __init__(self):
        pass

    def start(self):
        chrome.getInstance().doAction(message='Open facebook', action='open', params={'url': setting.getInstance().get('FACEBOOK')})
        chrome.getInstance().doAction(message='Waiting for loaded', action='wait_for_pageload')
        chrome.getInstance().doAction(action='setValue', params={'name': 'email', 'value': setting.getInstance().get('FACEBOOK_USER')})
        chrome.getInstance().doAction(action='setValue', params={'name': 'pass', 'value': setting.getInstance().get('FACEBOOK_PASSWORD')})
        chrome.getInstance().doAction(message='Waiting for login', action='wait_for_pageload')
        chrome.getInstance().doAction(message='Login facebook', action='click', params={'tag': 'input', 'text': 'login_form_login_button'})
        chrome.getInstance().doAction(message='Waiting for login', action='wait_for_pageload')
        chrome.getInstance().doAction(message='Remove notification dialog', action='click', params={'tag': 'button', 'text': 'Not Now'})
        # html = chrome.getInstance().getHtml()
        # soup = Beautifulsoup(content)

    def analysis(self):
        pass