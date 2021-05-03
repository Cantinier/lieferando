import pytest
from Steps.RestaurantsCatalog.RestaurantsCatalogSteps import get_restaurant_name_from_page, \
                                            open_category_on_restpage, \
                                            get_products_names, \
                                            get_product_card_by_name, add_product_in_cart_without_settings,\
                                            get_setting_container_by_product, \
                                            get_bucket_button_in_ingr_menu
from Steps.Basket.BasketSteps import get_basket_products_names, \
                                            get_count_prd_from_basket_by_name, \
                                            get_delete_button_from_basket_by_name
from Decorators.Preconditions import open_restaurants_page
from Data.restaurants import Restaurant
from Data.products import Product


@open_restaurants_page
def test_check_restpage(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C4. When clicking on the card opens the restaurant page
    """
    restaurant = Restaurant()
    target_restaurants = restaurant.get_restaurant_name()
    restaurant_name = get_restaurant_name_from_page(get_driver)
    assert target_restaurants in restaurant_name.text, \
        "When clicking on the restaurant's card, the restaurant page should open"


@open_restaurants_page
def test_check_product_on_restpage(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C5. The restaurant page contains goods affordable.
    """
    product = Product()
    target_product = product.get_product_with_settings()
    open_category_on_restpage(get_driver, "Burger")
    products_names = get_products_names(get_driver)
    products_names_list = []
    for element in products_names:
        products_names_list.append(element.find_element_by_tag_name('span').text)
    assert target_product in products_names_list, \
        "The restaurant page must contain a product card."


@open_restaurants_page
def test_add_product_without_settings(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C6. When clicking on the goods without settings - the product is added to the order basket
    """
    product = Product()
    target_product = product.get_product_without_settings()
    add_product_in_cart_without_settings(get_driver, "Alkoholfreie Getränke", target_product)
    basket_products_names = get_basket_products_names(get_driver)
    products_names_list = []
    for element in basket_products_names:
        products_names_list.append(element.text)
    assert target_product in products_names_list, \
        "When clicking on a product card without ingredient - the product must be added to the basket"


@open_restaurants_page
def test_add_product_increase(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C11. When you click on the goods without settings again - the amount of this product in the basket
        increases by 1
    """
    product = Product()
    target_product = product.get_product_without_settings()
    target_count = 2
    add_product_in_cart_without_settings(get_driver, "Alkoholfreie Getränke", target_product, count=target_count)
    count = get_count_prd_from_basket_by_name(get_driver, target_product)
    count = count.text[:count.text.find("x")]
    assert int(count) == target_count, \
        "When you repeatedly click on the product card without ingredient - the number in the basket increases by 1"


@open_restaurants_page
def test_open_ingredients_menu(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C7. When clicking on the goods with additional ingredients - the ingredients menu opens
    """
    product = Product()
    target_product = product.get_product_with_settings()
    product_card = get_product_card_by_name(get_driver, target_product)
    product_card.click()
    setting_container = get_setting_container_by_product(get_driver, product_card)
    assert setting_container, \
        "The product card must contain the ingredients menu"


@open_restaurants_page
def test_ingredients_menu_has_button(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C8. The ingredients menu contains the add button to the order basket.
    """
    product = Product()
    target_product = product.get_product_with_settings()
    product_card = get_product_card_by_name(get_driver, target_product)
    product_card.click()
    button = get_bucket_button_in_ingr_menu(get_driver, product_card)
    assert button, \
        "The ingredients menu must contain the addition button to the basket."


@open_restaurants_page
def test_add_product_with_settings(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C9. When clicking on the add button to the cart of goods in the ingredients menu - item
        is added to the order basket
    """
    product = Product()
    target_product = product.get_product_with_settings()
    product_card = get_product_card_by_name(get_driver, target_product)
    product_card.click()
    button = get_bucket_button_in_ingr_menu(get_driver, product_card)
    button.submit()
    basket_products_names = get_basket_products_names(get_driver)
    products_names_list = []
    for element in basket_products_names:
        products_names_list.append(element.text)
    assert target_product in products_names_list, \
        "When clicking on the add button - the goods must be added to the basket"


@open_restaurants_page
def test_item_in_bucket_has_delete_button(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C12. The goods added to the order basket contains a product removal button from the basket
    """
    product = Product()
    target_product = product.get_product_without_settings()
    add_product_in_cart_without_settings(get_driver, "Alkoholfreie Getränke", target_product)
    delete_btn = get_delete_button_from_basket_by_name(get_driver, target_product)
    assert delete_btn, \
        "Products in the basket have the \"Delete\" button"


@open_restaurants_page
def test_item_delete_from_cart(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C10.  	When clicking on the product removal button from the order basket - the goods
        are removed from the basket
    """
    product = Product()
    target_product = product.get_product_without_settings()
    add_product_in_cart_without_settings(get_driver, "Alkoholfreie Getränke", target_product)
    delete_btn = get_delete_button_from_basket_by_name(get_driver, target_product)
    print(delete_btn)
    delete_btn.click()
    basket_products_names = get_basket_products_names(get_driver)
    products_names_list = []
    for element in basket_products_names:
        products_names_list.append(element.text)
    assert target_product not in products_names_list, \
        "When clicking on the \"Delete\" button, the goods must be removed from the basket"
