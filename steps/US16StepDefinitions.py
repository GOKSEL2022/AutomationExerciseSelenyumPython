import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Navigate to url \'http://automationexercise.com\'')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://automationexercise.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)


@when(u'Click Signup_Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@href='/login']").click()


@when(u'Fill email password and click Login button')
def step_impl(context):
    email_address_login_your_account_login = context.driver.find_element(By.XPATH, "(//input[@name='email'])[1]")
    email_address_login_your_account_login.send_keys("gokselcelik@gmail.com")
    password_login_your_account_login = context.driver.find_element(By.XPATH, "//*[@data-qa='login-password']")
    password_login_your_account_login.send_keys("123456")
    login_button_your_account_login = context.driver.find_element(By.XPATH, "//*[@data-qa='login-button']")
    login_button_your_account_login.click()


@when(u'Verify Logged in as username at top')
def step_impl(context):
    logged_username_text_account_create = context.driver.find_element(By.XPATH, "//*[.='goksel celik']")
    assert logged_username_text_account_create.is_displayed(), "Logged in as username is visible"


@when(u'Add products to cart')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,150)", "")
    urun_ekle_ilk = context.driver.find_element(By.XPATH, "(//*[text()='Add to cart'])[1]")
    urun_ekle_ilk.click()
    continue_shopping_button_home = context.driver.find_element(By.XPATH,
                                                                "//*[@class='btn btn-success close-modal btn-block']")
    continue_shopping_button_home.click()
    time.sleep(1)
    urun_ekle_ikinci = context.driver.find_element(By.XPATH, "(//*[@data-product-id='2'])[1]")
    urun_ekle_ikinci.click()
    continue_shopping_button_home.click()


@when(u'Click Cart button')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,-300)", "")
    time.sleep(2)
    cart_button = context.driver.find_element(By.XPATH, "//*[@href='/view_cart']")
    cart_button.click()


@when(u'Verify that cart page is displayed')
def step_impl(context):
    sepet_sayfasi = context.driver.find_element(By.XPATH, "//*[text()='Shopping Cart']")
    assert sepet_sayfasi.is_displayed(), "Sepet sayfasindasiniz"


@when(u'Click Proceed To Checkout')
def step_impl(context):
    proceed_to_checkout_button_viewcart = context.driver.find_element(By.XPATH,
                                                                      "//*[@class='btn btn-default check_out']")
    proceed_to_checkout_button_viewcart.click()


@when(u'Verify Address Details and Review Your Order')
def step_impl(context):
    address_details_text_checkout = context.driver.find_element(By.XPATH, "//*[.='Address Details']")
    assert address_details_text_checkout.is_displayed(), "Address Details sayfasindasiniz"
    your_delivery_address_firstname_lastname_checkout = context.driver.find_element(By.XPATH,
                                                                                    "(//*[@class='address_firstname"
                                                                                    " address_lastname'])[1]")
    assert your_delivery_address_firstname_lastname_checkout.is_displayed(), "YOUR DELIVERY ADDRESS Mr. Göksel Çelik"
    your_billing_address_firstname_lastname_checkout = context.driver.find_element(By.XPATH,
                                                                                   "(//*[@class='address_firstname "
                                                                                   "address_lastname'])[1]")
    assert your_billing_address_firstname_lastname_checkout.is_displayed(), "YOUR BILLING ADDRESS Mr. Göksel Çelik"


@when(u'Enter description in comment text area and click Place Order')
def step_impl(context):
    time.sleep(1)
    comment_text_area_textbox_checkout = context.driver.find_element(By.XPATH, "//*[@class='form-control']")
    comment_text_area_textbox_checkout.send_keys("Aldiğim ürünlerden memnun kaldim ,tekrar görüşmek üzere ")
    place_order_button_checkout = context.driver.find_element(By.XPATH, "//*[@href='/payment']")
    place_order_button_checkout.click()

@when(u'Enter payment details Name on Card Card Number CVC Expiration date')
def step_impl(context):
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

    @when(u'Click Pay and Confirm Order button')
    def step_impl(context):
        pay_and_confirm_order_button = context.driver.find_element(By.XPATH, "//*[@data-qa='pay-button']")
        pay_and_confirm_order_button.click()

    @when(u'Verify success message Your order has been placed successfully')
    def step_impl(context):
        your_order_has_been_placed_successfully_alert = context.driver.find_element(By.XPATH,
                                                                                    "(//*[@class='alert-success alert'])[1]")
        assert your_order_has_been_placed_successfully_alert.is_displayed()

    @when(u'Click Pay and Confirm Order button')
    def step_impl(context):
        pay_and_confirm_order_button=context.driver.find_element(By.XPATH, "//*[@data-qa='pay-button']")
        pay_and_confirm_order_button.click()


