import time

from behave import *
from  selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Navigate to url "https://www.automationexercise.com/"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://automationexercise.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)


@when(u'Click on Signup_Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@href='/login']").click()

@when(u'Verify New User Signup is visible')
def step_impl(context):
    textNewUserSignup=context.driver.find_element(By.XPATH,"//*[text()='New User Signup!']")
    assert textNewUserSignup.is_displayed(), "New User Signup görünür."

@when(u'Enter name and email address')
def step_impl(context):
    nameNewUserSignupLogin=context.driver.find_element(By.XPATH, "//*[@name='name']")
    nameNewUserSignupLogin.send_keys("ahmetcelebi")
    time.sleep(2)
    emailAddressNewUserSignupLogin = context.driver.find_element(By.XPATH, "//*[@data-qa='signup-email']")
    emailAddressNewUserSignupLogin.send_keys("ahmetcelebi@gmail.com")
    time.sleep(1)

@when(u'Click Signup button')
def step_impl(context):
    signupButtonNewUserSignupLogin=context.driver.find_element(By.XPATH, "//*[@data-qa='signup-button']")
    signupButtonNewUserSignupLogin.click()

@when(u'Verify that ENTER ACCOUNT INFORMATION is visible')
def step_impl(context):
    enterAccountInformationTextSignup = context.driver.find_element(By.XPATH, "(//*[.='Enter Account Information'])[2]")
    assert enterAccountInformationTextSignup.is_displayed(), "ENTER ACCOUNT INFORMATION sayfasindasin"

@when(u'Fill details Title Name Email Password Date of birth')
def step_impl(context):
    radioButtonMrSignup=context.driver.find_element(By.XPATH, "//*[@id='id_gender1']")
    radioButtonMrSignup.click()
    time.sleep(1)
    signupPasswordSignup=context.driver.find_element(By.XPATH, "//input[@data-qa='password']")
    signupPasswordSignup.send_keys("123456")
    time.sleep(1)
    signupDaySignup=context.driver.find_element(By.XPATH, "//*[@name='days']")
    signupDaySignup.send_keys("10")
    time.sleep(1)
    signupMonthSignup=context.driver.find_element(By.XPATH, "//*[@id='months']")
    signupMonthSignup.send_keys("January")
    time.sleep(1)
    signupYearsSignup=context.driver.find_element(By.XPATH, "//*[@id='years']")
    signupYearsSignup.send_keys("1990")

@when(u'Select checkbox Sign up for our newsletter')
def step_impl(context):
    newsletterCheckboxSignup=context.driver.find_element(By.XPATH, "//*[@id='newsletter']")
    newsletterCheckboxSignup.click()

@when(u'Select checkbox Receive special offers from our partners')
def step_impl(context):
    receivePartnersCheckboxSignup=context.driver.find_element(By.XPATH, "//*[@name='optin']")
    receivePartnersCheckboxSignup.click()


@when(u'Fill details First name Last name Company Address Address2 Country State City Zipcode Mobile Number')
def step_impl(context):
    firstnameTextboxSignup =context.driver.find_element(By.XPATH, "//*[@id='first_name']")
    firstnameTextboxSignup.send_keys("Göksel")
    time.sleep(1)
    lastnameTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='last_name']")
    lastnameTextboxSignup.send_keys("Çelik")
    time.sleep(1)
    companyTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='company']")
    companyTextboxSignup.send_keys("Çelik Yazilim Test A.Ş.")
    time.sleep(1)
    addressTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='address1']")
    addressTextboxSignup.send_keys("Susam Sokağı TRT Apartmani")
    time.sleep(1)
    addressTwoTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='address2']")
    addressTwoTextboxSignup.send_keys("Daire : Edi ve Büdü ")
    time.sleep(1)
    countryDropdownSignup=context.driver.find_element(By.XPATH, "//*[@id='country']")
    countryDropdownSignup.send_keys("Canada")
    time.sleep(1)
    stateTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='state']")
    stateTextboxSignup.send_keys("Çankaya")
    time.sleep(1)
    cityTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='city']")
    cityTextboxSignup.send_keys("Ankara")
    time.sleep(1)
    zipCodeTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='zipcode']")
    zipCodeTextboxSignup.send_keys("5255")
    time.sleep(1)
    mobileNumberTextboxSignup=context.driver.find_element(By.XPATH, "//*[@id='mobile_number']")
    mobileNumberTextboxSignup.send_keys("05948534840")
    time.sleep(2)
    createAccountButtonSignup=context.driver.find_element(By.XPATH, "(//*[@class='btn btn-default'])[1]")
    createAccountButtonSignup.click()


@when(u'Verify that ACCOUNT CREATED is visible')
def step_impl(context):
    createAccountTextAccountCreate=context.driver.find_element(By.XPATH, "(//*[.='Account Created!'])[2]")
    assert createAccountTextAccountCreate.is_displayed(), "ACCOUNT CREATED görünür."

@when(u'Click Continue button')
def step_impl(context):
    accountContinueButtonAccountCreate=context.driver.find_element(By.XPATH, "//div[@class='pull-right']")
    accountContinueButtonAccountCreate.click()
    context.driver.refresh()
    time.sleep(1)
    accountContinueButtonAccountCreate.click()

@when(u'Verify that Logged in as username is visible')
def step_impl(context):
    loggedUsernameTextAccountCreate=context.driver.find_element(By.XPATH, "//*[.='ahmetcelebi']")
    assert loggedUsernameTextAccountCreate.is_displayed(), "Logged in as username is visible"

@when(u'Click Delete Account button')
def step_impl(context):
    deleteAccountButtonAccountCreate=context.driver.find_element(By.XPATH, "(//*[.=' Delete Account'])[2]")
    deleteAccountButtonAccountCreate.click()
@when(u'Verify that ACCOUNT DELETED is visible and click Continue button')
def step_impl(context):
    accountDeletedTextAccountCreate=context.driver.find_element(By.XPATH, "(//*[.='Account Deleted!'])[2]")
    assert accountDeletedTextAccountCreate.is_displayed(), "ACCOUNT DELETED is visible"










