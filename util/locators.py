from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def find_by_xpath(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
    return driver.find_element_by_xpath(path)


def find_by_id(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, path)))
    return driver.find_element_by_id(path)
