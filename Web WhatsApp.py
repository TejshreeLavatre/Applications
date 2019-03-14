"""A simple program to open web WhatsApp, select a person from your chat list, and send them a message"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
web = webdriver.Chrome()
web.get('http://web.whatsapp.com')
web.implicitly_wait(20)
elem = web.find_element_by_xpath('//span[contains(text(), "TJ")]')  #Replace "TJ" with your contact's name
web.maximize_window()
elem.click()
input = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
input.send_keys("Tejshree")                                         #Replace "Tejshree" with your personal message
input.send_keys(Keys.ENTER)
