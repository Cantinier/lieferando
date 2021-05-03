from selenium.webdriver.common.by import By


def get_search_input(driver):
    SearchInput = driver.find_element(By.XPATH, '//*[@id="imysearchstring"]')
    return SearchInput


def click_on_search_input(driver):
    SearchInput = get_search_input(driver)
    SearchInput.click()


def add_address_on_search_input(driver, address):
    SearchInput = get_search_input(driver)
    SearchInput.click()
    SearchInput.send_keys(address)
    return SearchInput


def get_autocomplete_dropdown_elements(driver):
    driver.implicitly_wait(5)
    DropDown = driver.find_element(By.XPATH, '//*[@id="iautoCompleteDropDownContent"]')
    DropDownElements = DropDown.find_elements_by_tag_name('a')
    return DropDownElements
