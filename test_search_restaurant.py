import pytest
from Steps.MainPage.MainPageSteps import get_search_input, \
                                            add_address_on_search_input, \
                                            get_autocomplete_dropdown_elements
from Steps.RestaurantsCatalog.RestaurantsCatalogSteps import get_restaurants_list_names
from Data.addresses import addresses_C2, addresses_C3
from Data.restaurants import restaurants


def test_availability_of_string(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C1. On the main page there is an input line for the address
    """
    assert get_search_input(get_driver), \
        "The main page must contain the address entry string"


def test_check_target_address(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C2. When entering data in the search string, autocomplete works
    """
    nearest_address, target_address = addresses_C2[0].values()
    add_address_on_search_input(get_driver, nearest_address)
    DropDownElements = get_autocomplete_dropdown_elements(get_driver)
    DropDownElementsList = []
    for element in DropDownElements:
        DropDownElementsList.append(element.text)
    assert target_address in DropDownElementsList, \
        "When entering the address, the drop-down list of suitable addresses should be displayed."


def test_check_nearest_restaurant(get_driver):
    """
    :param get_driver: pytest.fixture to start / stop the browser
    Case Automation C3. When choosing a address - a list of nearest restaurants is displayed
    """
    target_address = addresses_C3[0]
    target_restaurants = restaurants[0]
    add_address_on_search_input(get_driver, target_address)
    DropDownElements = get_autocomplete_dropdown_elements(get_driver)
    for element in DropDownElements:
        if element.text == target_address:
            element.click()
            break
    restaurants_names = get_restaurants_list_names(get_driver)
    restaurants_names_list = []
    for element in restaurants_names:
        restaurants_names_list.append(element.text)
    assert target_restaurants in restaurants_names_list, \
        "When clicking on the address, the catalog of the desired restaurants should open"

