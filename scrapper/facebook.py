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

# face book login 
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

    def parse(self):
        with open("element/ruman.html", encoding="utf-8") as f:
            data = f.read()
            soup = BeautifulSoup(data, 'html.parser')
            # div = soup.select('div[id^=PagesProfileAboutInfoPagelet_]')
            div_profile = soup.select('div[id^= PagesProfileAboutInfoPagelet_]')
            for div in div_profile:
                # div_profile_children = div.findChildren('div', recursive=True)
                div_profile_children = div.find_all('div', recursive=False)

            # print("type:",type(div_profile_children))
            
            if len(div_profile_children) > 0:
                # print("lensof profile",len(div_profile_children))
                div_find_us = div_profile_children[1]
                div_business_info = div_profile_children[2]
            
            mail_address = ""
            mail_tag = soup.select('a[href^= mailto]')
            if len(mail_tag) > 0:
                for mail in mail_tag:
                    mail_address += mail.text
            mail_address = mail_address.strip()
            print(mail_address)           
    
    def find_us(self, section_find_us):
        # print(section_find_us)
        div_find_us = section_find_us.findChildren('div',recursive=False)[0].findChildren('div',recursive=False)[0].findChildren('div', recursive=False)[0].findChildren('div', recursive=False)
       
        #FIND US div div_find_us[0]
        div_title = div_find_us[0].find('span')
        if div_title.text == "FIND US":
            print("find us correnct")

                
        # Address Div div_find_us[1]
        div_address = div_find_us[1].findChildren('div',recursive=False)
        full_address = ""
        for address in div_address[1].find_all('div'):
            full_address += address.text + "  "
            full_address = full_address.strip()
            print(address.text)
        # print("full-address", full_address)

        # Phone Div div_find_us[3]
        call_phone = ""
        for phone in div_find_us[3].findChildren('div', recursive=False):
            call_phone += phone.text
            
        call_phone = call_phone.strip()
        print("stripeed", call_phone)