import util.locators as locators
import util.elementsLandingPage as elementsLandingPage


def check_url(driver, landing_page_url):
    locators.find_by_xpath(driver, elementsLandingPage.header_text_XPATH)
    assert driver.current_url + "#" == landing_page_url


def pick_amount_50(driver):
    locators.find_by_xpath(driver, elementsLandingPage.amount_50_XPATH).click()


def pick_amount_100(driver):
    locators.find_by_xpath(driver, elementsLandingPage.amount_100_XPATH).click()


def pick_amount_150(driver):
    locators.find_by_xpath(driver, elementsLandingPage.amount_150_XPATH).click()


def pick_and_fill_amount_other(driver, amount):
    locators.find_by_xpath(driver, elementsLandingPage.amount_other_XPATH).click()
    locators.find_by_xpath(driver, elementsLandingPage.amount_other_input_XPATH).send_keys(amount)


def fill_your_email_address(driver, customer_email):
    locators.find_by_xpath(driver, elementsLandingPage.my_email_input_element_XPATH).send_keys(customer_email)


def fill_your_first_name(driver, first_name):
    locators.find_by_xpath(driver, elementsLandingPage.first_name_input_XPATH).send_keys(first_name)


def fill_your_last_name(driver, last_name):
    locators.find_by_xpath(driver, elementsLandingPage.last_name_input_XPATH).send_keys(last_name)


def click_on_send_someone_else(driver):
    locators.find_by_xpath(driver, elementsLandingPage.sent_to_someone_else_XPATH).click()


def fill_recipient_email(driver, recipient_email):
    locators.find_by_xpath(driver, elementsLandingPage.recipient_email_input_XPATH).send_keys(recipient_email)


def fill_message_for_recipient(driver, message_to_recipient):
    locators.find_by_xpath(driver, elementsLandingPage.recipient_message_input_XPATH).send_keys(message_to_recipient)


def click_to_checkout(driver):
    locators.find_by_xpath(driver, elementsLandingPage.checkout_button_element_XPATH).click()
