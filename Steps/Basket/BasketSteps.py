from selenium.webdriver.common.by import By


def get_basket_products_names(driver):
    driver.implicitly_wait(10)
    basket_products = driver.find_element(By.XPATH, '//*[@id="products"]')
    basket_products_names = basket_products.find_elements_by_class_name('cart-meal-name')
    return basket_products_names


def get_count_prd_from_basket_by_name(driver, name):
    basket_products_names = get_basket_products_names(driver)
    for element in basket_products_names:
        if element.text == name:
            parent = element.find_element(By.XPATH, './..')
            count = parent.find_element_by_class_name('cart-meal-amount')
            break
    return count


def get_delete_button_from_basket_by_name(driver, name):
    basket_products_names = get_basket_products_names(driver)
    for element in basket_products_names:
        if element.text == name:
            parent = element.find_element(By.XPATH, './..')
            delete_btn = parent.find_element_by_class_name('cart-meal-delete')
            break
    return delete_btn
