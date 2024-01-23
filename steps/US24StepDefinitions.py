import time

import faker
from faker import Faker
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@when(u'Click Register_Login button')
def step_impl(context):
    register_login_link_viewcart = context.driver.find_element(By.XPATH, "(//*[@href='/login'])[2]")
    register_login_link_viewcart.click()


@when(u'Fill all details in Signup and create account')
def step_impl(context):
    faker = Faker()
    random_name = faker.name()
    random_email = faker.email()
    name_new_user_signup_login = context.driver.find_element(By.XPATH, "//*[@name='name']")
    name_new_user_signup_login.send_keys(random_name)
    time.sleep(2)
    email_address_new_user_signup_login = context.driver.find_element(By.XPATH, "//*[@data-qa='signup-email']")
    email_address_new_user_signup_login.send_keys(random_email)
    time.sleep(1)
    signup_button_new_user_signup_login = context.driver.find_element(By.XPATH, "//*[@data-qa='signup-button']")
    signup_button_new_user_signup_login.click()
