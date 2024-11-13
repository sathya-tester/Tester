from selenium import webdriver
from selenium.webdriver.common.by import By
def setup():
    # set the chromeOptions

    option = webdriver.ChromeOptions()
    option.add_experimental_option(name='detach', value=True)
    driver = webdriver.Chrome(option)
    return driver

import Pytest
def  test():
    driver=setup()
    driver.maximize_window()
    driver.get('https://www.facebook.com')
    # to validation assertions


    createPage=driver.find_element(By.XPATH,"//a[@href='/pages/create/?ref_type=registration_form']")
    text=createPage.text
    result=createPage.is_enabled()
    assert 'Create a Page' in text
    assert  True is result
    createPage.click()