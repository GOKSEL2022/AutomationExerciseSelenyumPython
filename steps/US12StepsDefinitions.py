import re
import time

from behave import *
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




@given(u'Navigate to url "http://automationexercise.com"')
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.get("http://automationexercise.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)



@when(u'Verify that home page is visible successfully')
def step_impl(context):
    assert "Automation Exercise" == context.driver.title
    #context.driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")

@when(u'Click Products button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[text()=' Products']").click()
    context.driver.refresh()
    context.driver.find_element(By.XPATH, "//*[text()=' Products']").click()

@when(u'Hover over first product and click Add to cart')
def step_impl(context):

    context.driver.execute_script("window.scrollBy(0,150)", "")
    context.driver.find_element(By.XPATH ,"(//*[text()='Add to cart'])[1]").click()
    #print("ilk urun sepete eklendi")


@when(u'Click Continue Shopping button')
def step_impl(context):
    #context.driver.find_element_by_xpath(By.XPATH, "//*[@class='btn btn-success close-modal btn-block']").click()
    context.driver.find_element(By.XPATH ,"//*[@class='btn btn-success close-modal btn-block']").click()
    # print("alisverise devam et buton tiklandi")
    time.sleep(3)

@when(u'Hover over second product and click Add to cart')
def step_impl(context):
    context.driver.find_element(By.XPATH ,"(//*[@data-product-id='2'])[1]").click()
    context.driver.find_element(By.XPATH ,"//*[@class='btn btn-success close-modal btn-block']").click()

@when(u'Click View Cart button')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,-300)", "")
    time.sleep(2)
    context.driver.find_element(By.XPATH ,"(//*[.=' Cart'])[1]").click()
    time.sleep(2)

@when(u'Verify both products are added to Cart')
def step_impl(context):
    link = context.driver.current_url
    if "view_cart" in link:
        print("tebrikler,sepet sayfasindasiniz")
        time.sleep(2)


    blueTopProductViewCart = context.driver.find_element(By.XPATH ,"//*[.='Women > Tops']")
    blueTopProductViewCart.is_displayed()
    menTshirtProductViewCart = context.driver.find_element(By.XPATH ,"//*[.='Men > Tshirts']")
    menTshirtProductViewCart.is_displayed()

@then(u'Verify their prices quantity and total price')
def step_impl(context):
    blue_top_cart_price_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='cart_price'])[1]").text)
    blue_top_cart_price_int = int(blue_top_cart_price_str)

    blue_top_total_price_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='cart_total_price'])[1]").text)
    blue_top_total_price_int = int(blue_top_total_price_str)

    men_tshirt_cart_price_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='cart_price'])[2]").text)
    men_tshirt_cart_price_int = int(men_tshirt_cart_price_str)

    men_tshirt_total_price_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='cart_total_price'])[2]").text)
    men_tshirt_total_price_int = int(men_tshirt_total_price_str)

    quantity_women_text_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='disabled'])[1]").text)
    quantity_women_text_int = int(quantity_women_text_str)

    quantity_men_tshirts_str = re.sub(r'\D', '',
    context.driver.find_element(By.XPATH ,"(//*[@class='disabled'])[1]").text)
    quantity_men_tshirts_int = int(quantity_men_tshirts_str)

    assert blue_top_cart_price_int * quantity_women_text_int == blue_top_total_price_int
    assert men_tshirt_cart_price_int * quantity_men_tshirts_int == men_tshirt_total_price_int
    context.driver.close()




