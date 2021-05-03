from selenium.webdriver.common.by import By


def get_restaurants_list_names(driver):
    driver.implicitly_wait(10)
    restaurants_list = driver.find_element(By.XPATH, '//*[@id="irestaurantlist"]')
    restaurants_list_names = restaurants_list.find_elements_by_tag_name('a')
    return restaurants_list_names


def get_restaurant_name_from_page(driver):
    driver.implicitly_wait(10)
    restaurant_name = driver.find_element_by_class_name("restaurant-name")
    return restaurant_name


def open_category_on_restpage(driver, category):
    driver.implicitly_wait(10)
    restaurant_categories_container = driver.find_element_by_class_name("menu-category-list")
    restaurants_categories = restaurant_categories_container.find_elements_by_tag_name('a')
    for element in restaurants_categories:
        if element.text == category:
            element.click()
            break


def get_products_names(driver):
    driver.implicitly_wait(10)
    restaurant_products = driver.find_elements_by_class_name("meal-name")
    return restaurant_products


def get_product_card_by_name(driver, name):
    driver.implicitly_wait(10)
    restaurant_products = driver.find_elements_by_class_name("meal-container")
    for element in restaurant_products:
        meal_name = element.find_element_by_class_name("meal-name")
        if meal_name.find_element_by_tag_name('span').text == name:
            print(element.get_attribute('id'))
            return element


def get_setting_container_by_product(driver, product_card):
    driver.implicitly_wait(10)
    product_id = product_card.get_attribute('id')
    try:
        product_setting_base_container = product_card.find_element(By.ID, ("sidedishesproductform"+product_id))
        product_setting_inner_container = product_setting_base_container.find_element_by_class_name("inner")
        return product_setting_inner_container
    except Exception:
        return None


def add_product_in_cart_without_settings(driver, catalog, product, count=1):
    open_category_on_restpage(driver, catalog)
    product_card = get_product_card_by_name(driver, product)
    if product_card is not None:
        for i in range(0, count):
            product_card.click()


def get_bucket_button_in_ingr_menu(driver, product_card):
    setting_container = get_setting_container_by_product(driver, product_card)
    button = setting_container.find_element_by_class_name("cartbutton-button")
    return button
