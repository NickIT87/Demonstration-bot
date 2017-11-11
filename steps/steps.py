#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from pages import pageClasses


#_____________Global step - get page url_____________

@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.maximize_window()
    context.driver.get(pageClasses.Base.ADRESS)

#_____________First step - show about text___________

@then('i learn more and redirect to features page')
def step_learn_more(context):
    main_page = pageClasses.MainPage(context.driver)
    main_page.learnMore()

#_____________Second step - test features____________

@then('i work with features cypher {text}, {key}, {cryptmsg}')
def step_test_cypher(context, text, key, cryptmsg):
    features_page = pageClasses.FeaturesPage(context.driver)
    features_page.tabRewiev()
    features_page.testCrypt(text, key)
    features_page.testDecrypt(cryptmsg, key)

#_____________Third step - test features_____________

@then('i work with features bot {textstart}, {ansvone}, {ansvtwo}, {ansvthree}')
def step_test_cypher(context, textstart, ansvone, ansvtwo, ansvthree):
    features_page = pageClasses.FeaturesPage(context.driver)
    features_page.testBot(textstart, ansvone, ansvtwo, ansvthree)
    features_page.testBot2(textstart, ansvtwo, ansvthree)
