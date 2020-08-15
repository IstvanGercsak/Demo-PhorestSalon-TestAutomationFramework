import util.locators as locators
import util.elementsSummaryPage as elementsSummaryPage


def check_url(driver, summary_page_url):
    locators.find_by_xpath(driver, elementsSummaryPage.header_text_XPATH)
    assert driver.current_url == summary_page_url


def click_on_edit(driver):
    locators.find_by_xpath(driver, elementsSummaryPage.click_on_edit_button_XPATH).click()


def check_value_of_gift_card(driver, value):
    value_element = locators.find_by_xpath(driver, elementsSummaryPage.value_of_gift_card_XPATH)
    assert value_element.text == value


def check_send_receipt_to(driver, test_customer_email_address):
    receipt_to_element = locators.find_by_xpath(driver, elementsSummaryPage.send_receipt_to_XPATH)
    assert receipt_to_element.text == test_customer_email_address


def check_send_gift_card_to(driver, test_customer_email_address):
    send_it_to = locators.find_by_xpath(driver, elementsSummaryPage.send_gift_card_to_XPATH)
    assert send_it_to.text == test_customer_email_address


def click_on_confirm_details_button(driver):
    locators.find_by_xpath(driver, elementsSummaryPage.confirm_details_button_XPATH).click()
