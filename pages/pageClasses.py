#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class Base(unittest.TestCase):
    #initialize webdriver and inherit metods from unittest
    def __init__(self, driver):
        super(Base, self).__init__()
        self.driver = driver
    #global method - find and return element if this element is visible
    def findVisibleElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located(locator))
        return element    
    #global method - find and return element if this element is present in DOM
    def findElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located(locator))
        return element
    #global method - find and return list of elements if this elements is present in DOM
    def findElems(self, locator):
        elements = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_all_elements_located(locator))
        return elements
    #global method - Check text present in element
    def checkTextPresentInElem(self, locator, text):
        WebDriverWait(self.driver,10).\
            until(expected_conditions.text_to_be_present_in_element(locator, text))
    #locators    
    ADRESS = 'http://localhost:8000/'
   

class MainPage(Base):
    #locators
    LEARN_MORE_BTN = (By.ID,"showbut")
    IMG_TERMINATOR = (By.NAME,"terminator")
    MODAL_IMG = (By.ID,"modalimg")

    def learnMore(self):
        time.sleep(5)
        lmbtn = self.findElement(self.LEARN_MORE_BTN)
        lmbtn.click()
        time.sleep(3)
        self.driver.execute_script \
            ("function vniz() { window.scrollBy(0,2); if (window.pageYOffset < 725) {requestAnimationFrame(vniz);} } vniz();")
        time.sleep(10)
        imgterm = self.findElement(self.IMG_TERMINATOR)
        imgterm.click()
        time.sleep(5)
        modalimg = self.findVisibleElement(self.MODAL_IMG)
        modalimg.click()
        time.sleep(1)
        self.driver.execute_script("window.open('http://localhost:8000/features.html','_blank');")

        
class FeaturesPage(Base):
    #locators
    TXT_FIELD_1 = (By.ID,"text1")
    KEY_FIELD_1 = (By.ID,"key1")
    ENCRYPT_BTN = (By.ID,"btn1")
    TXT_FIELD_2 = (By.ID,"text2")
    KEY_FIELD_2 = (By.ID,"key2")
    DECRYPT_BTN = (By.ID,"btn2")
    TXT_FIELD_BOT = (By.ID,"txt")
    BUTTON_BOT = (By.ID,"btn")
    TAB2 = (By.XPATH,'//*[@id="cryptprg"]/ul/li[2]/a/span')
    TAB3 = (By.XPATH,'//*[@id="cryptprg"]/ul/li[3]/a/span')

    def tabRewiev(self):
        window_feature = self.driver.window_handles[1]
        self.driver.switch_to.window(window_feature)
        time.sleep(5)
        fastrack = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.TAB2))
        fastrack.click()
        time.sleep(4)
        fastrack = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.TAB3))
        fastrack.click()
        time.sleep(4)
        

    def testCrypt(self, text, key):
        #window_feature = self.driver.window_handles[1]
        #self.driver.switch_to.window(window_feature)
        txt_field1 = self.findElement(self.TXT_FIELD_1)
        txt_field1.send_keys(text)
        key_field1 = self.findElement(self.KEY_FIELD_1)
        key_field1.send_keys(key)
        encrypt_btn = self.findElement(self.ENCRYPT_BTN)
        encrypt_btn.click()
        time.sleep(5)

    def testDecrypt(self, cryptmsg, key):
        #window_feature = self.driver.window_handles[1]
        #self.driver.switch_to.window(window_feature)
        txt_field2 = self.findElement(self.TXT_FIELD_2)
        txt_field2.send_keys(cryptmsg)
        key_field2 = self.findElement(self.KEY_FIELD_2)
        key_field2.send_keys(key)
        decrypt_btn = self.findElement(self.DECRYPT_BTN)
        decrypt_btn.click()
        time.sleep(5)

    def testBot(self, textstart, ansvone, ansvtwo, ansvthree):
        txt_field_bot = self.findElement(self.TXT_FIELD_BOT)
        txt_field_bot.send_keys(textstart)
        button_bot = self.findElement(self.BUTTON_BOT)
        button_bot.click()
        time.sleep(5)
        txt_field_bot.send_keys(ansvtwo)
        button_bot.click()
        time.sleep(5)
        for i in range(3):
            txt_field_bot.send_keys(ansvone)
            button_bot.click()
            time.sleep(5)
        txt_field_bot.send_keys(ansvthree)
        button_bot.click()
        time.sleep(5)

    def testBot2(self, textstart, ansvtwo, ansvthree):
        txt_field_bot = self.findElement(self.TXT_FIELD_BOT)
        txt_field_bot.send_keys(textstart)
        button_bot = self.findElement(self.BUTTON_BOT)
        button_bot.click()
        time.sleep(5)
        for i in range(4):
            txt_field_bot.send_keys(ansvtwo)
            button_bot.click()
            time.sleep(5)
        txt_field_bot.send_keys(ansvthree)
        button_bot.click()
        time.sleep(10)
        #self.driver.execute_script("window.open('http://localhost:8000/resume.html','_blank');")

