import os
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


@when(u'Verify ACCOUNT CREATED and click Continue button')
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
    newsletter_checkbox_signup = context.driver.find_element(By.XPATH, "//*[@id='newsletter']")
    newsletter_checkbox_signup.click()
    receive_partners_checkbox_signup = context.driver.find_element(By.XPATH, "//*[@name='optin']")
    receive_partners_checkbox_signup.click()
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
    time.sleep(2)
    create_account_text_account_create = context.driver.find_element(By.XPATH, "(//*[.='Account Created!'])[2]")
    assert create_account_text_account_create.is_displayed(), "ACCOUNT CREATED görünür."
    time.sleep(1)
    account_continue_button_account_create = context.driver.find_element(By.XPATH, "//div[@class='pull-right']")
    account_continue_button_account_create.click()
    context.driver.refresh()
    account_continue_button_account_create2 = context.driver.find_element(By.XPATH, "//div[@class='pull-right']")
    account_continue_button_account_create2.click()

    logged_username_text_account_create = context.driver.find_element(By.XPATH, "//*[text()=' Logged in as ']")
    assert logged_username_text_account_create.is_displayed(), "Logged in as username is visible"

    cart_button = context.driver.find_element(By.XPATH, "//*[@href='/view_cart']")
    cart_button.click()


@when(u'Click Proceed To Checkout button')
def step_impl(context):
    proceed_to_checkout_button_viewcart = context.driver.find_element(By.XPATH,
                                                                      "//*[@class='btn btn-default check_out']")
    proceed_to_checkout_button_viewcart.click()
    time.sleep(1)
    your_delivery_address_firstname_lastname_checkout = context.driver.find_element(By.XPATH,
                                                                                    "(//*[@class='address_firstname"
                                                                                    " address_lastname'])[1]")
    assert your_delivery_address_firstname_lastname_checkout.is_displayed(), "YOUR DELIVERY ADDRESS Mr. Göksel Çelik"

    time.sleep(1)
    comment_text_area_textbox_checkout = context.driver.find_element(By.XPATH, "//*[@class='form-control']")
    comment_text_area_textbox_checkout.send_keys("Aldiğim ürünlerden memnun kaldim ,tekrar görüşmek üzere ")
    place_order_button_checkout = context.driver.find_element(By.XPATH, "//*[@href='/payment']")
    place_order_button_checkout.click()

    time.sleep(1)
    name_on_card_textbox_payment = context.driver.find_element(By.XPATH, "//*[@data-qa='name-on-card']")
    name_on_card_textbox_payment.send_keys("Göksel")
    card_number_textbox_payment = context.driver.find_element(By.XPATH, "//*[@data-qa='card-number']")
    card_number_textbox_payment.send_keys("5255")
    cvc_textbox_payment = context.driver.find_element(By.XPATH, "//*[@data-qa='cvc']")
    cvc_textbox_payment.send_keys("123")
    mm_textbox_payment = context.driver.find_element(By.XPATH, "//*[@data-qa='expiry-month']")
    mm_textbox_payment.send_keys("12")
    yyyy_textbox_payment = context.driver.find_element(By.XPATH, "//*[@data-qa='expiry-year']")
    yyyy_textbox_payment.send_keys("2024")
    pay_and_confirm_order_button = context.driver.find_element(By.XPATH, "//*[@data-qa='pay-button']")
    pay_and_confirm_order_button.click()


@when(u'Click Download Invoice button and verify invoice is downloaded successfully')
def step_impl(context):
    download_invoice_button_payment=context.driver.find_element(By.XPATH, "//*[.='Download Invoice']")
    download_invoice_button_payment.click()
    time.sleep(3)
    downloaded_file = "C:\\Users\\Lenovo\\Downloads\\invoice.txt"
    assert os.path.exists(downloaded_file),"Dosya bulunamadi"
    print("Dosya basarili sekilde indirildi")

