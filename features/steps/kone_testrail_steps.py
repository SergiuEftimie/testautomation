from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# start the browser
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(chrome_options=chrome_options)

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['chromeOptions'] = {'args': ['--start-maximized']}
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=capabilities)

@given(u'a user is on the testrail login page')
def step_impl(context):
    driver.get('https://kone.testrail.com/index.php?/auth/login/')

@when(u'the user types "{email}" in the Email field')
def step_impl(context,email):
    element = driver.find_element_by_xpath("//input[@id='name']")
    element.send_keys(email)

@when(u'the user types "{password}" in the Password field')
def step_impl(context,password):
    element = driver.find_element_by_xpath("//input[@id='password']")
    element.send_keys(password)

@when(u'the user unchecks the "Keep me logged in" checkbox')
def step_impl(context,email):
    element = driver.find_element_by_xpath("//span[@class='loginpage-checkmark']")
    element.click()

@when(u'the user clicks on the Login button')
def step_impl(context):
    element = driver.find_element_by_xpath("//button[@id='button_primary']")
    element.click()

@when(u'the user clicks on the top right Add Test Suite button')
def step_impl(context):
    element = driver.find_element_by_xpath("//span[text()='Add Test Suite']")
    element.click()

@step(u'the user is redirected to the testrail home page')
def step_impl(context):
    element = driver.find_element_by_xpath("//a[@id='navigation-dashboard']")

@when(u'the user clicks on the Test Suites link')
def step_impl(context):
    element = driver.find_element_by_xpath("//a[text()='Test Suites']")
    element.click()

@when(u'the user types "{testSuiteName}" in the name field')
def step_impl(context,testSuiteName):
    element = driver.find_element_by_xpath("//input[@name='name']")
    element.send_keys(testSuiteName)

@when(u'the user types "{description}" in the description field')
def step_impl(context,description):
    element = driver.find_element_by_xpath("//textarea[@name='description']")
    element.send_keys(description)

@when(u'the user clicks on the Add Test Suite button')
def step_impl(context):
    element = driver.find_element_by_xpath("//button[@id='accept']")
    element.click()

@then(u'the test suite is created')
def step_impl(context):
    element = driver.find_element_by_xpath("//div[contains(text(),'Successfully added the new test suite.')]")
    assert element.text == "Successfully added the new test suite."

@when(u'the user clicks on Test User')
def step_impl(context):
    element = driver.find_element_by_xpath("//span[text()='Test User']")
    element.click()

@then(u'the user clicks on Logout')
def step_impl(context):
    element = driver.find_element_by_xpath("//a[@class='dropdown-menu-link' and text()='Logout']")
    element.click()

@then(u'the user is logged out')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is logged out')

@then('close the browser')
def step_impl5(context):
    driver.close()
    driver.quit()