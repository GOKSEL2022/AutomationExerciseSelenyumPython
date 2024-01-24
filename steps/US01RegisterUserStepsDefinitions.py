import time

import faker
from faker import Faker
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Navigate to url "https://www.automationexercise.com/"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://automationexercise.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)


@when(u'Click on Signup_Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@href='/login']").click()


@when(u'Verify New User Signup is visible')
def step_impl(context):
    text_new_user_signup = context.driver.find_element(By.XPATH, "//*[text()='New User Signup!']")
    assert text_new_user_signup.is_displayed(), "New User Signup görünür."


@when(u'Enter name and email address')
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


@when(u'Click Signup button')
def step_impl(context):
    signup_button_new_user_signup_login = context.driver.find_element(By.XPATH, "//*[@data-qa='signup-button']")
    signup_button_new_user_signup_login.click()


@when(u'Verify that ENTER ACCOUNT INFORMATION is visible')
def step_impl(context):
    enter_account_information_text_signup = context.driver.find_element(By.XPATH, "(//*[.='Enter Account Information'])[2]")
    assert enter_account_information_text_signup.is_displayed(), "ENTER ACCOUNT INFORMATION sayfasindasin"


@when(u'Fill details Title Name Email Password Date of birth')
def step_impl(context):
    radio_button_mr_signup = context.driver.find_element(By.XPATH, "//*[@id='id_gender1']")
    radio_button_mr_signup.click()
    time.sleep(1)
    signup_password_signup = context.driver.find_element(By.XPATH, "//input[@data-qa='password']")
    signup_password_signup.send_keys("123456")
    time.sleep(1)
    signup_day_signup = context.driver.find_element(By.XPATH, "//*[@name='days']")
    signup_day_signup.send_keys("10")
    time.sleep(1)
    signup_month_signup = context.driver.find_element(By.XPATH, "//*[@id='months']")
    signup_month_signup.send_keys("January")
    time.sleep(1)
    signup_years_signup = context.driver.find_element(By.XPATH, "//*[@id='years']")
    signup_years_signup.send_keys("1990")


@when(u'Select checkbox Sign up for our newsletter')
def step_impl(context):
    newsletter_checkbox_signup = context.driver.find_element(By.XPATH, "//*[@id='newsletter']")
    newsletter_checkbox_signup.click()


@when(u'Select checkbox Receive special offers from our partners')
def step_impl(context):
    receive_partners_checkbox_signup = context.driver.find_element(By.XPATH, "//*[@name='optin']")
    receive_partners_checkbox_signup.click()


@when(u'Fill details First name Last name Company Address Address2 Country State City Zipcode Mobile Number')
def step_impl(context):
    firstname_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='first_name']")
    firstname_textbox_signup.send_keys("Göksel")
    time.sleep(1)
    lastname_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='last_name']")
    lastname_textbox_signup.send_keys("Çelik")
    time.sleep(1)
    company_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='company']")
    company_textbox_signup.send_keys("Çelik Yazilim Test A.Ş.")
    time.sleep(1)
    address_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='address1']")
    address_textbox_signup.send_keys("Susam Sokağı TRT Apartmani")
    time.sleep(1)
    address_two_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='address2']")
    address_two_textbox_signup.send_keys("Daire : Edi ve Büdü ")
    time.sleep(1)
    country_dropdown_signup = context.driver.find_element(By.XPATH, "//*[@id='country']")
    country_dropdown_signup.send_keys("Canada")
    time.sleep(1)
    state_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='state']")
    state_textbox_signup.send_keys("Çankaya")
    time.sleep(1)
    city_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='city']")
    city_textbox_signup.send_keys("Ankara")
    time.sleep(1)
    zip_code_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='zipcode']")
    zip_code_textbox_signup.send_keys("5255")
    time.sleep(1)
    mobile_number_textbox_signup = context.driver.find_element(By.XPATH, "//*[@id='mobile_number']")
    mobile_number_textbox_signup.send_keys("05948534840")
    time.sleep(2)
    create_account_button_signup = context.driver.find_element(By.XPATH, "(//*[@class='btn btn-default'])[1]")
    create_account_button_signup.click()


@when(u'Verify that ACCOUNT CREATED is visible')
def step_impl(context):
    create_account_text_account_create = context.driver.find_element(By.XPATH, "(//*[.='Account Created!'])[2]")
    assert create_account_text_account_create.is_displayed(), "ACCOUNT CREATED görünür."


@when(u'Click Continue button')
def step_impl(context):
    account_continue_button_account_create = context.driver.find_element(By.XPATH, "//div[@class='pull-right']")
    account_continue_button_account_create.click()
    context.driver.refresh()
    account_continue_button_account_create2=context.driver.find_element(By.XPATH, "//div[@class='pull-right']")
    account_continue_button_account_create2.click()


@when(u'Verify that Logged in as username is visible')
def step_impl(context):
    logged_username_text_account_create = context.driver.find_element(By.XPATH, "//*[text()=' Logged in as ']")
    assert logged_username_text_account_create.is_displayed(), "Logged in as username is visible"


@when(u'Click Delete Account button')
def step_impl(context):
    delete_account_button_account_create = context.driver.find_element(By.XPATH, "(//*[@style='color:brown;'])[2]")
    delete_account_button_account_create.click()


@when(u'Verify that ACCOUNT DELETED is visible and click Continue button')
def step_impl(context):
    account_deleted_text_account_create = context.driver.find_element(By.XPATH, "//*[@class='title text-center']")
    assert account_deleted_text_account_create.is_displayed(), "ACCOUNT DELETED is visible"
    continue_button = context.driver.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    continue_button.click()
