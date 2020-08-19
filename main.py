from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
import pyautogui

link = ""
time = 10
driver = webdriver.Firefox()
driver.get(link)
message = ""
for i in range(1, time):
    text_filed = driver.find_element_by_id("ask_content")
    text_filed.click()
    text_filed.send_keys(message)

    button = driver.find_element_by_class_name("ask_bottom_buttom")
    button.click()
    sleep(1.5)
    alert = driver.switch_to.alert
    alert.accept()
    sleep(1.5)
