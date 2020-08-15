import logging
from selenium import webdriver
import unittest
import testdata.test_data as testdata
import pages.demoLandingPage as landingPage
import pages.demoSummaryPage as summaryPage
import pages.demoPaymentPage as paymentPage
import pages.demoConfirmPage as confirmPage
import util.check_email as check_email
from pyunitreport import HTMLTestRunner

# Configuring logging level and webdriver path
logging.basicConfig(
    filename="log/test_log.log",
    level=logging.INFO,
    format='%(asctime)s: %(levelname)s: %(message)s ',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

# Test pages url
landing_page_url = 'https://gift-cards.phorest.com/salons/demo-us#'
summary_page_url = "https://gift-cards.phorest.com/salons/demo-us#confirm"
payment_page_url = "https://gift-cards.phorest.com/salons/demo-us#payment"
confirm_payment_url = "https://gift-cards.phorest.com/salons/demo-us#success"

# Test data
test_customer = testdata.Customer("test-custumer.prvnbtvf@mailosaur.io", "Istvan", "Gercsak")
test_recipient_email = "test-recipient.ylz3dti2@mailosaur.io"
test_message_to_recipient = "Test message"

# Valid test card
valid_test_card = testdata.Card("Istvan Gercsak", 92606, 4111111111111111, 1222, 999)


class Test(unittest.TestCase):

    # Instantiate the webdriver and get the first page url before every test run
    def setUp(self):
        self.driver = webdriver.Chrome('webdriver/chromedriver')
        self.driver.get(landing_page_url)
        self.driver.maximize_window()
        logging.info("============================TEST============================")
        logging.info("URL: " + self.driver.current_url)
        logging.info("Title: " + self.driver.title)

    def test_pay_50_for_me(self):
        logging.info(self)

        test_pay_amount_50 = "$50"

        # Landing page
        landingPage.pick_amount_50(self.driver)
        landingPage.fill_your_email_address(self.driver, test_customer.email_address)
        landingPage.fill_your_first_name(self.driver, test_customer.first_name)
        landingPage.fill_your_last_name(self.driver, test_customer.last_name)
        landingPage.click_to_checkout(self.driver)

        # Summary page
        summaryPage.check_url(self.driver, summary_page_url)
        summaryPage.check_value_of_gift_card(self.driver, test_pay_amount_50)
        summaryPage.check_send_receipt_to(self.driver, test_customer.email_address)
        summaryPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        summaryPage.click_on_confirm_details_button(self.driver)

        # Payment page
        paymentPage.check_url(self.driver, payment_page_url)
        paymentPage.check_value_of_gift_card(self.driver, test_pay_amount_50)
        paymentPage.check_send_receipt_to(self.driver, test_customer.email_address)
        paymentPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        paymentPage.fill_card_details(self.driver, valid_test_card)
        paymentPage.click_on_submit_button(self.driver)

        # Confirm page
        confirmPage.check_url(self.driver, confirm_payment_url)
        logging.info("Your gift card code is: " + confirmPage.get_gift_card_code(self.driver))
        logging.info("Your gift card value is: " + confirmPage.get_gift_card_value(self.driver, test_pay_amount_50))
        confirmPage.click_on_done_button(self.driver)

        landingPage.check_url(self.driver, landing_page_url)

    def test_pay_100_for_me(self):
        logging.info(self)

        test_pay_amount_100 = "$100"

        # Landing page
        landingPage.pick_amount_100(self.driver)
        landingPage.fill_your_email_address(self.driver, test_customer.email_address)
        landingPage.fill_your_first_name(self.driver, test_customer.first_name)
        landingPage.fill_your_last_name(self.driver, test_customer.last_name)
        landingPage.click_to_checkout(self.driver)

        # Summary page
        summaryPage.check_url(self.driver, summary_page_url)
        summaryPage.check_value_of_gift_card(self.driver, test_pay_amount_100)
        summaryPage.check_send_receipt_to(self.driver, test_customer.email_address)
        summaryPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        summaryPage.click_on_confirm_details_button(self.driver)

        # Payment page
        paymentPage.check_url(self.driver, payment_page_url)
        paymentPage.check_value_of_gift_card(self.driver, test_pay_amount_100)
        paymentPage.check_send_receipt_to(self.driver, test_customer.email_address)
        paymentPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        paymentPage.fill_card_details(self.driver, valid_test_card)
        paymentPage.click_on_submit_button(self.driver)

        # Confirm page
        confirmPage.check_url(self.driver, confirm_payment_url)
        logging.info("Your gift card code is: " + confirmPage.get_gift_card_code(self.driver))
        logging.info("Your gift card value is: " + confirmPage.get_gift_card_value(self.driver, test_pay_amount_100))
        confirmPage.click_on_done_button(self.driver)

        landingPage.check_url(self.driver, landing_page_url)

    def test_pay_for_me_other_amount_256(self):
        logging.info(self)

        test_pay_amount_256 = "$256"

        # Landing page
        landingPage.pick_and_fill_amount_other(self.driver, 256)
        landingPage.fill_your_email_address(self.driver, test_customer.email_address)
        landingPage.fill_your_first_name(self.driver, test_customer.first_name)
        landingPage.fill_your_last_name(self.driver, test_customer.last_name)
        landingPage.click_to_checkout(self.driver)

        # Summary page
        summaryPage.check_url(self.driver, summary_page_url)
        summaryPage.check_value_of_gift_card(self.driver, test_pay_amount_256)
        summaryPage.check_send_receipt_to(self.driver, test_customer.email_address)
        summaryPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        summaryPage.click_on_confirm_details_button(self.driver)

        # Payment page
        paymentPage.check_url(self.driver, payment_page_url)
        paymentPage.check_value_of_gift_card(self.driver, test_pay_amount_256)
        paymentPage.check_send_receipt_to(self.driver, test_customer.email_address)
        paymentPage.check_send_gift_card_to(self.driver, test_customer.email_address)
        paymentPage.fill_card_details(self.driver, valid_test_card)
        paymentPage.click_on_submit_button(self.driver)

        # Confirm page
        confirmPage.check_url(self.driver, confirm_payment_url)
        logging.info("Your gift card code is: " + confirmPage.get_gift_card_code(self.driver))
        logging.info("Your gift card value is: " + confirmPage.get_gift_card_value(self.driver, test_pay_amount_256))
        confirmPage.click_on_done_button(self.driver)

        landingPage.check_url(self.driver, landing_page_url)

    def test_pay_150_for_someone_else(self):
        logging.info(self)

        test_pay_amount_150 = "$150"

        # Landing page
        landingPage.click_on_send_someone_else(self.driver)
        landingPage.pick_amount_150(self.driver)
        landingPage.fill_recipient_email(self.driver, test_recipient_email)
        landingPage.fill_message_for_recipient(self.driver, test_message_to_recipient)
        landingPage.fill_your_email_address(self.driver, test_customer.email_address)
        landingPage.fill_your_first_name(self.driver, test_customer.first_name)
        landingPage.fill_your_last_name(self.driver, test_customer.last_name)
        landingPage.click_to_checkout(self.driver)

        # Summary page
        summaryPage.check_url(self.driver, summary_page_url)
        summaryPage.check_value_of_gift_card(self.driver, test_pay_amount_150)
        summaryPage.check_send_receipt_to(self.driver, test_customer.email_address)
        summaryPage.check_send_gift_card_to(self.driver, test_recipient_email)
        summaryPage.click_on_confirm_details_button(self.driver)

        # Payment page
        paymentPage.check_url(self.driver, payment_page_url)
        paymentPage.check_value_of_gift_card(self.driver, test_pay_amount_150)
        paymentPage.check_send_receipt_to(self.driver, test_customer.email_address)
        paymentPage.check_send_gift_card_to(self.driver, test_recipient_email)
        paymentPage.fill_card_details(self.driver, valid_test_card)
        paymentPage.click_on_submit_button(self.driver)

        # Confirm page
        confirmPage.check_url(self.driver, confirm_payment_url)
        logging.info("Your gift card code is: " + confirmPage.get_gift_card_code(self.driver))
        logging.info("Your gift card value is: " + confirmPage.get_gift_card_value(self.driver, test_pay_amount_150))
        confirmPage.click_on_done_button(self.driver)

        landingPage.check_url(self.driver, landing_page_url)

    def test_pay_other_amount_256_for_someone_else_and_check_email_sent(self):
        logging.info(self)

        test_pay_amount_256 = "$256"

        # Landing page
        landingPage.click_on_send_someone_else(self.driver)
        landingPage.pick_and_fill_amount_other(self.driver, 256)
        landingPage.fill_recipient_email(self.driver, test_recipient_email)
        landingPage.fill_message_for_recipient(self.driver, test_message_to_recipient)
        landingPage.fill_your_email_address(self.driver, test_customer.email_address)
        landingPage.fill_your_first_name(self.driver, test_customer.first_name)
        landingPage.fill_your_last_name(self.driver, test_customer.last_name)
        landingPage.click_to_checkout(self.driver)

        # Summary page
        summaryPage.check_url(self.driver, summary_page_url)
        summaryPage.check_value_of_gift_card(self.driver, test_pay_amount_256)
        summaryPage.check_send_receipt_to(self.driver, test_customer.email_address)
        summaryPage.check_send_gift_card_to(self.driver, test_recipient_email)
        summaryPage.click_on_confirm_details_button(self.driver)

        # Payment page
        paymentPage.check_url(self.driver, payment_page_url)
        paymentPage.check_value_of_gift_card(self.driver, test_pay_amount_256)
        paymentPage.check_send_receipt_to(self.driver, test_customer.email_address)
        paymentPage.check_send_gift_card_to(self.driver, test_recipient_email)
        paymentPage.fill_card_details(self.driver, valid_test_card)
        paymentPage.click_on_submit_button(self.driver)

        # Confirm page
        confirmPage.check_url(self.driver, confirm_payment_url)
        logging.info("Your gift card code is: " + confirmPage.get_gift_card_code(self.driver))
        logging.info("Your gift card value is: " + confirmPage.get_gift_card_value(self.driver, test_pay_amount_256))
        confirmPage.click_on_done_button(self.driver)

        check_email.check_emails_arrives(test_customer.email_address, test_recipient_email)

        landingPage.check_url(self.driver, landing_page_url)

    # Close the browser after every run
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='report'))
