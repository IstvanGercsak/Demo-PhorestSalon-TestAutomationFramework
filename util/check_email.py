from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
import logging
from time import sleep

client = MailosaurClient("Og76hkjJXz189ll")

# Configuring logging level and webdriver path
logging.basicConfig(
    filename="log/test_log.log",
    level=logging.INFO,
    format='%(asctime)s: %(levelname)s: %(message)s ',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


def check_emails_arrives(customer_email, recipient_email):
    # Build search criteria to find the email you have sent
    criteria_for_customer = SearchCriteria()
    criteria_for_recipient = SearchCriteria()

    criteria_for_customer.sent_to = customer_email
    criteria_for_recipient.sent_to = recipient_email

    # Wait for the message (by default only looks for messages received in the last hour)
    test_email = client.messages.get("prvnbtvf", criteria_for_customer)
    test_email_recipient = client.messages.get("ylz3dti2", criteria_for_recipient)

    # Wait for the email to be arrived
    sleep(10)
    # Assert that the email subject is what we expect

    logging.info("Receipt email subject: " + test_email.subject)
    logging.info("Gift card email subject: " + test_email_recipient.subject)
    assert "Your Receipt for Arden Courts" == test_email.subject
    assert "You've been sent a $256 gift card for Demo US!" == test_email_recipient.subject
