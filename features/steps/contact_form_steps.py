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

@given('a user is on the main page')
def step_impl1(context):
    driver.get('https://www.isoskills.fi')

@when('the user types "{text}" in the "{fieldName}" contact field')
def step_impl2(context,text,fieldName):
    element = driver.find_element_by_xpath("//label[contains(text(),'"+fieldName+"')]/span/input")
    element.send_keys(text)

@when('the user types "{text}" in the "{fieldName}" text area')
def step_impl2(context,text,fieldName):
    element = driver.find_element_by_xpath("//label[contains(text(),'"+fieldName+"')]/span/textarea")
    element.send_keys(text)

@when('the user clicks on the send button')
def step_impl3(context):
    element = driver.find_element_by_xpath("//input[@value='Send']")
    element.click()
    
@then('the "{text}" text is displayed')
def step_impl4(context, text):
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'"+text+"')]")))
    assert element.text == text

@then('close the browser')
def step_impl5(context):
    driver.close()
    driver.quit()

@when('the user clicks on the "{link}" link')
def step_impl(context,link):
    xpath = "//span[@class='link-inner'][contains(text(),'"+link+"')]/parent::a"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()

@when('the user clicks on the "{buttonText}" button for the "{article}" article')
def step_impl(context,article,buttonText):
    xpath = "//div/h4[contains(text(),'"+article+"')]//parent::div/following-sibling::div/a[@title='"+buttonText+"']"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()

@then('the "{articleTitle}" article is opened')
def step_impl(context,articleTitle):
    xpath ="//h1[@class='single-post-title entry-title' and contains(text(),'"+articleTitle+"')]"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    assert element.text == articleTitle

@when('the user searches for "{searchTerm}" using the search field')
def step_impl(context,searchTerm):
    searchXpath = "//span[@class='wpex-menu-search-icon ticon ticon-search']"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, searchXpath)))
    element.click()
    searchField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@class='field' and @type='search']")))
    searchField.send_keys(searchTerm)
    searchField.send_keys(Keys.RETURN)

@then('the "{resultTitle}" appears in the results list')
def step_impl(context,resultTitle):
    xpath = "//div[@class='search-entry-text']//a[contains(text(),'"+resultTitle+"')]"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    assert element.text == resultTitle

@when('the user clicks on the "{socialButton}" social button')
def step_impl(context,socialButton):
    xpath = "//a[@title='"+socialButton+"']"
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()

@then('the user is redirected to the "{url}" page')
def step_impl(context,url):
    driver.switch_to.window(driver.window_handles[1])
    currentUrl = driver.current_url
    assert currentUrl == url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def scrollIntoView(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)