import util.locators as locators
import util.elementsPaymentPage as elementsPaymentPage


def check_url(driver, payment_page_url):
    locators.find_by_xpath(driver, elementsPaymentPage.header_text_XPATH)
    assert driver.current_url == payment_page_url


def check_value_of_gift_card(driver, value):
    value_element = locators.find_by_xpath(driver, elementsPaymentPage.value_of_gift_card_XPATH)
    assert value_element.text == value


def check_send_receipt_to(driver, test_customer_email_address):
    receipt_to_element = locators.find_by_xpath(driver, elementsPaymentPage.send_receipt_to_XPATH)
    assert receipt_to_element.text == test_customer_email_address


def check_send_gift_card_to(driver, test_customer_email_address):
    send_it_to = locators.find_by_xpath(driver, elementsPaymentPage.send_gift_card_to_XPATH)
    assert send_it_to.text == test_customer_email_address


def fill_card_details(driver, valid_test_card):
    iframe_locator_id = locators.find_by_xpath(driver, elementsPaymentPage.payment_form_id).get_attribute("id")
    driver.switch_to.frame(iframe_locator_id)

    locators.find_by_id(driver, elementsPaymentPage.cardholder_name_input_ID).send_keys(valid_test_card.cardholder_name)
    locators.find_by_id(driver, elementsPaymentPage.zip_code_input_ID).send_keys(valid_test_card.zip_code)
    locators.find_by_id(driver, elementsPaymentPage.card_number_input_ID).send_keys(valid_test_card.card_number)
    locators.find_by_id(driver, elementsPaymentPage.expiry_date_input_ID).send_keys(valid_test_card.valid_til)
    locators.find_by_id(driver, elementsPaymentPage.cvc_code_input_ID).send_keys(valid_test_card.cvc)


def click_on_submit_button(driver):
    locators.find_by_id(driver, elementsPaymentPage.submit_ID).click()
