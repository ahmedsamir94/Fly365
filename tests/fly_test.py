from selenium import webdriver
import pytest
import time
from pages.Search_Page import SearchPage
from pages.SignUp_Page import SignUpPage
from pages.ContactUs_Page import ContactUsPage
from utils import utils as utils

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:/ahmed testing/tools/Fly365_Tests/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")

def test_search(test_setup):
    driver.get(utils.URL)
    driver.implicitly_wait(5)

    search=SearchPage(driver)
    search.enter_origin(utils.ORIGIN_POINT)
    time.sleep(1)
    search.enter_destination(utils.DESTINATION)
    time.sleep(1)
    search.enter_date_time()
    time.sleep(1)
    search.click_search()


def test_SignUp(test_setup):
    driver.get(utils.URL)
    driver.implicitly_wait(5)

    SignUp=SignUpPage(driver)
    SignUp.click_SignUp()
    SignUp.enter_first_name(utils.FIRSTNAME)
    SignUp.enter_family_name(utils.FAMILYNAME)
    SignUp.enter_email(utils.EMAIL)
    SignUp.enter_password(utils.PASSWORD)
    SignUp.create_account()
    SignUp.click_account()
    SignUp.click_SignOut()
    SignUp.enter_username(utils.USERNAME)
    SignUp.enter_Password(utils.PASS)

def test_ContactUs(test_setup):
    driver.get(utils.URL)
    driver.implicitly_wait(5)

    ContactUs=ContactUsPage(driver)
    ContactUs.click_ContacUs()
    ContactUs.enter_FullName(utils.FULLNAME)
    ContactUs.enter_email(utils.EMAIL)
    ContactUs.click_category()
    ContactUs.select_category()
    ContactUs.enter_mesage(utils.MESSAGE)
    ContactUs.click_send()