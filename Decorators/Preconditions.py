from Data.addresses import addresses_C3
from Data.restaurants import restaurants
from Steps.MainPage.MainPageSteps import add_address_on_search_input, \
                                            get_autocomplete_dropdown_elements
from Steps.RestaurantsCatalog.RestaurantsCatalogSteps import get_restaurants_list_names


def open_restaurants_page(test):
    def open_restaurants_page_func(get_driver):
        target_address = addresses_C3[0]
        target_restaurants = restaurants[0]
        add_address_on_search_input(get_driver, target_address)
        DropDownElements = get_autocomplete_dropdown_elements(get_driver)
        for element in DropDownElements:
            if element.text == target_address:
                element.click()
                break
        restaurants_names = get_restaurants_list_names(get_driver)
        for element in restaurants_names:
            if element.text == target_restaurants:
                element.click()
                break
        test(get_driver)
    return open_restaurants_page_func

