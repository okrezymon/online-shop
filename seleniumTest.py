from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
from selenium.webdriver.chrome.options import Options


#ChromeOptions = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(executable_path=r'/opt/chromedriver_linux64/chromedriver', chrome_options=chrome_options)
actions = webdriver.ActionChains(driver)


def i_go_to_main_page():
    driver.maximize_window()
    driver.get("http://127.0.0.1/kursy-online")
    assert "kursy-online" in driver.title



def i_choose_product_by_clicking_on_image(course_name):
    product_image_xpath = "//div[@class='products row']/div/article/div/a[img[@alt='${course_name}']]"
    product = driver.find_element(By.XPATH, product_image_xpath.replace("${course_name}", course_name))
    product.click()
    actions.pause(1).perform()


def i_increase_quantity_to_by_clicking_up_button(quantity):
    qty_btn_up_xpath = "//button[contains(@class, 'btn') and contains(@class, 'bootstrap-touchspin-up')]"
    product_qty_up = driver.find_element(By.XPATH, qty_btn_up_xpath)
    for i in range(quantity-1):
        product_qty_up.click()
        actions.pause(1).perform()


def i_add_product_to_the_cart():
    driver.find_element(By.CLASS_NAME, "add-to-cart").click()
    actions.pause(1).perform()


def i_verify_if_the_product_was_added_to_the_cart():
    i_wait_for_element_visibility((By.XPATH, "//div[@id='blockcart-modal' and contains(@style, 'display: block')]"), 10)
    purchase_info = driver.find_element(By.ID, "myModalLabel").get_property("childNodes")
    assert purchase_info[1]['textContent'] == "Produkt dodany poprawnie do Twojego koszyka"
    actions.pause(1).perform()


def i_click_go_back_to_the_shop_button():
    cart_content = driver.find_element(By.CLASS_NAME, "cart-content-btn")
    cart_content.find_element(By.TAG_NAME, "button").click()
    actions.pause(1).perform()


def i_go_to_category_using_navigation_panel(category):
    category_xpath = "//ul/li/a[normalize-space(.) ='${category}']"
    driver.find_element(By.XPATH, category_xpath.replace("${category}", category)).click()
    actions.pause(1).perform()


def i_go_to_next_page_on_product_list():
    current_page = int(driver.find_element(By.XPATH, "//li[@class='current']/a").text)
    driver.find_element(By.XPATH, "//li/a[contains(normalize-space(.),'Następny')]").click()
    next_page_xpath = "//li[@class='current']/a[normalize-space(.)='${page}']".replace("${page}", str(current_page+1))
    i_wait_for_element_visibility((By.XPATH, next_page_xpath), 10)
    actions.pause(1).perform()


def i_choose_product_on_page(product_name):
    product_name_xpath = "//div[@class='product-description']/h2/a[normalize-space(.)='${product_name}']"
    driver.find_element(By.XPATH, product_name_xpath.replace("${product_name}", product_name)).click()
    actions.pause(1).perform()


def i_set_quantity_to(quantity):
    qty = driver.find_element(By.ID, "quantity_wanted")
    qty.send_keys(Keys.ARROW_RIGHT, Keys.BACKSPACE, quantity)
    actions.pause(1).perform()


def i_search_for_product_in_search_bar(searched_product):
    search_bar = driver.find_element(By.NAME, "s")
    search_bar.send_keys(searched_product)
    search_bar.send_keys(Keys.ENTER)
    actions.pause(1).perform()


def i_check_search_result_and_i_select_the_product_if_available():
    products_on_page = driver.find_elements(By.CLASS_NAME, "product")
    assert (len(products_on_page) == 1)
    i_select_product_through_quick_view(products_on_page)
    actions.pause(1).perform()


def i_select_product_through_quick_view(product_list):
    product = product_list[0].find_element(By.XPATH, "//div[contains(@class, 'highlighted-informations')]/a")
    actions.move_to_element(product).perform()
    product.click()
    i_wait_for_element_visibility((By.XPATH, "//div[contains(@id, 'quickview-modal') and contains(@style, 'display: block')]"), 10)


def i_choose_product_option(option):
    product_option_xpath = "//li[contains(@class, 'input-container')]/label[span[.='${option}']]/input"
    driver.find_element(By.XPATH, product_option_xpath.replace("${option}", option)).click()
    actions.pause(1).perform()


def i_go_to_cart_summary():
    cart_content = driver.find_element(By.CLASS_NAME, "cart-content-btn")
    cart_content.find_element(By.TAG_NAME, "a").click()
    actions.pause(1).perform()


def i_remove_item_from_cart(item_name):
    item_xpath = "//ul[@class='cart-items']/li[.//a[.='${item_name}']]"
    item = driver.find_element(By.XPATH, item_xpath.replace("${item_name}", item_name))
    item.find_element(By.CLASS_NAME, "remove-from-cart").click()
    wait = WebDriverWait(driver, 10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.invisibility_of_element(item))
    products = driver.find_element(By.XPATH, "//ul[@class='cart-items']/li")
    assert len(products.size) == 2


def i_go_to_pay():
    driver.find_element(By.XPATH, "//div[contains(@class, 'cart-summary')]/div/div/a").click()
    actions.pause(1).perform()


def i_want_to_fill_form(form):
    return driver.find_element(By.ID, form)
    actions.pause(1).perform()


def i_set_title_name_to_ms(form):
    form.find_element(By.XPATH, "//div[label[normalize-space(.) = 'Nazwa kontaktu']]/div/label/span/input[@value=2]").click()
    actions.pause(1).perform()


def i_set_title_name_to_mr(form):
    form.find_element(By.XPATH, "//div[label[normalize-space(.) = 'Nazwa kontaktu']]/div/label/span/input[@value=1]").click()
    actions.pause(1).perform()


def i_set_field_to_on_form(field, value, form):
    form.find_element(By.NAME, field).send_keys(value)
    actions.pause(1).perform()


def i_check_option_on_form(option, form):
    form.find_element(By.NAME, option).click()
    actions.pause(1).perform()


def i_click_continue_button_on_form(form):
    form.find_element(By.CLASS_NAME, "continue").click()
    actions.pause(1).perform()


def i_choose_delivery_option_to(delivery_option, form):
    delivery_option_xpath = "//div[contains(@class, 'delivery-option')][.//span[contains(normalize-space(.),'DHL')]]/div/span/input"
    form.find_element(By.XPATH, delivery_option_xpath.replace("${delivery_option}", delivery_option)).click()
    actions.pause(1).perform()


def i_check_cart_totals():
    cost_of_products = driver.find_element(By.XPATH, "//div[@id='cart-subtotal-products']/span[2]").text.strip()
    cost_of_payment = driver.find_element(By.XPATH, "//div[@id='cart-subtotal-shipping']/span[2]").text.strip()
    total_cost = driver.find_element(By.XPATH, "//div[contains(@class,'cart-total')]/span[2]").text.strip()

    assert cost_of_products == "212,50 zł"
    assert cost_of_payment == "12,30 zł"
    assert total_cost == "224,80 zł"


def i_choose_payment_option_to(payment_option):
    payment_form = driver.find_element(By.CLASS_NAME, "payment-options")
    payment_option_xpath = "//div/div[label/span[normalize-space(.)='${payment-option}']]/span/input"
    payment_form.find_element(By.XPATH, payment_option_xpath.replace("${payment-option}", payment_option)).click()
    actions.pause(1).perform()


def i_confirm_terms_and_conditions():
    driver.find_element(By.XPATH, "//input[@name='conditions_to_approve[terms-and-conditions]']").click()
    actions.pause(1).perform()


def i_confirm_payment():
    driver.find_element(By.XPATH, "//div[@id='payment-confirmation']/div/button").click()
    confirmation = driver.find_element(By.XPATH, "//section[@id='content-hook_order_confirmation']//h3").get_property("childNodes")
    assert confirmation[2]['textContent'].strip() == "Twoje zamówienie zostało potwierdzone"
    actions.pause(1).perform()


def i_save_order_reference_number():
    order_number = driver.find_element(By.ID, "order-reference-value").text.replace("Numer zamówienia: ", "")
    return order_number


def i_go_to_user_panel():
    driver.find_element(By.CLASS_NAME, "account").click()
    actions.pause(1).perform()


def i_go_to_transaction_history():
    driver.find_element(By.ID, "history-link").click()
    actions.pause(1).perform()


def i_check_a_delivery_status(order_id):
    status_xpath = "//table/tbody/tr[th[.='${order_id}']]/td[count(//table/thead/tr/th[.='Wyświetlany']/preceding-sibling::th)]"
    status = driver.find_element(By.XPATH, status_xpath.replace("${order_id}", order_id)).text
    assert status.strip() == "Oczekiwanie na płatność przelewem"
    actions.pause(1).perform()


def i_log_out_from_account():
    driver.find_element(By.CLASS_NAME, "logout").click()
    actions.pause(1).perform()


def i_wait_for_element_visibility(element, sec):
    wait = WebDriverWait(driver, sec, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.presence_of_element_located(element))


def selenium_test():
    i_go_to_main_page()
    # buy first item
    i_go_to_category_using_navigation_panel("PROGRAMOWANIE")
    i_choose_product_by_clicking_on_image("Kurs Jak zacząć karierę w Data Science")
    i_increase_quantity_to_by_clicking_up_button(3)
    i_add_product_to_the_cart()
    i_verify_if_the_product_was_added_to_the_cart()
    i_click_go_back_to_the_shop_button()
    # buy second item
    i_go_to_category_using_navigation_panel("PROGRAMOWANIE")
    i_go_to_next_page_on_product_list()
    i_choose_product_on_page("Kurs Przetwarzanie języka...")
    i_set_quantity_to(2)
    i_add_product_to_the_cart()
    i_verify_if_the_product_was_added_to_the_cart()
    i_click_go_back_to_the_shop_button()
    # buy third item
    i_search_for_product_in_search_bar("Jak zarabiać przez internet jako freelancer")
    i_check_search_result_and_i_select_the_product_if_available()
    i_choose_product_option("Kurs bez certyfikacji")
    i_set_quantity_to(5)
    i_add_product_to_the_cart()
    i_verify_if_the_product_was_added_to_the_cart()
    # cart summary and item removal
    i_go_to_cart_summary()
    i_remove_item_from_cart("Jak zarabiać przez internet jako freelancer")
    i_go_to_pay()
    # filling contact form with registration
    customer_form = i_want_to_fill_form("customer-form")
    i_set_title_name_to_ms(customer_form)
    i_set_field_to_on_form("firstname", "Selenium", customer_form)
    i_set_field_to_on_form("lastname", "Test", customer_form)
    i_set_field_to_on_form("email", "test1@test", customer_form)
    i_set_field_to_on_form("password", "selenium1234", customer_form)
    i_set_field_to_on_form("birthday", "1997-10-11", customer_form)
    i_check_option_on_form("customer_privacy", customer_form)
    i_check_option_on_form("newsletter", customer_form)
    i_check_option_on_form("psgdpr", customer_form)
    i_click_continue_button_on_form(customer_form)
    # filling address form
    address_form = i_want_to_fill_form("delivery-address")
    i_set_field_to_on_form("address1", "Selenidowa 1/2", address_form)
    i_set_field_to_on_form("postcode", "12-345", address_form)
    i_set_field_to_on_form("city", "Gdańsk", address_form)
    i_set_field_to_on_form("phone", "123 456 789", address_form)
    i_click_continue_button_on_form(address_form)
    # filling delivery form
    delivery_form = i_want_to_fill_form("js-delivery")
    i_choose_delivery_option_to("DHL", delivery_form)
    i_click_continue_button_on_form(delivery_form)
    i_check_cart_totals()
    # filling payment form
    i_choose_payment_option_to("Zapłać przelewem")
    # confirm terms and conditions
    i_confirm_terms_and_conditions()
    # confirm payment
    i_confirm_payment()
    order_reference = i_save_order_reference_number()
    i_go_to_user_panel()
    i_go_to_transaction_history()
    i_check_a_delivery_status(order_reference)
    i_log_out_from_account()
    print("Test passed")


try:
    selenium_test()
except Exception as e:
    print(str(e))
    print("Test failure")
finally:
    driver.close()