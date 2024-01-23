

from behave import *
from  selenium import webdriver
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
    emailAddressLoginYourAccountLogin=context.driver.find_element(By.XPATH, "(//input[@name='email'])[1]")
    emailAddressLoginYourAccountLogin.send_keys("gokselcelik@gmail.com")
    passwordLoginYourAccountLogin=context.driver.find_element(By.XPATH, "//*[@data-qa='login-password']")
    passwordLoginYourAccountLogin.send_keys("123456")
    loginButtonYourAccountLogin=context.driver.find_element(By.XPATH, "//*[@data-qa='login-button']")
    loginButtonYourAccountLogin.click()

@when(u'Verify Logged in as username at top')
def step_impl(context):
    loggedUsernameTextAccountCreate = context.driver.find_element(By.XPATH, "//*[.='goksel celik']")
    assert loggedUsernameTextAccountCreate.is_displayed(), "Logged in as username is visible"



