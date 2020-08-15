import util.locators as locators
import util.elementsConfirmPage as elementsConfirmPage


def check_url(driver, confirm_payment_url):
    locators.find_by_xpath(driver, elementsConfirmPage.header_text_XPATH)
    assert driver.current_url == confirm_payment_url


def get_gift_card_code(driver):
    return locators.find_by_xpath(driver, elementsConfirmPage.gift_card_code_XPATH).text


def get_gift_card_value(driver, payable_amount):
    card_value = locators.find_by_xpath(driver, elementsConfirmPage.gift_card_value_XPATH)
    assert card_value.text == payable_amount
    return card_value.text


def click_on_done_button(driver):
    locators.find_by_xpath(driver, elementsConfirmPage.done_button_XPATH).click()
