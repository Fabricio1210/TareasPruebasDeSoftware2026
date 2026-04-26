# -*- coding: utf-8 -*-

"""
System Test example using Behavior-Driven Development (BDD) with Behave (Gherkin) and Selenium.
"""
from behave import given, then, when  # pylint: disable=no-name-in-module
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium import webdriver

@given("I am on DuckDuckGo")  # pylint: disable=not-callable
def open_browser(context):
    """Opens DuckDuckGo in the browser"""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.get("https://duckduckgo.com")


@when('I search for "{university_url}" on DuckDuckGo')
def search(context, university_url):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(university_url)
    search_box.send_keys(Keys.RETURN)

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "li[data-layout='organic'] a[data-testid='result-title-a']")
        )
    )


@when("I click the first result")
def click_first(context):
    wait = WebDriverWait(context.driver, 10)
    first_result = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "li[data-layout='organic'] a[data-testid='result-title-a']")
        )
    )
    first_result.click()

@then('I should be on the "{university_url}" website')
def verify_university(context, university_url):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains(university_url))
    assert university_url in context.driver.current_url

@when('I search for "{section}" inside the site')
def click_section(context, section):
    wait = WebDriverWait(context.driver, 15)
    link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"a[href*='{section}']"))
    )
    context.driver.execute_script("arguments[0].removeAttribute('target');", link)
    context.driver.execute_script("arguments[0].click();", link)
    wait.until(EC.url_contains(section))

@then('I should see the "{tab_id}" tab')
def scroll_to_tab(context, tab_id):
    wait = WebDriverWait(context.driver, 10)
    tab = wait.until(
        EC.visibility_of_element_located((By.ID, tab_id)) 
    )
    y_position = tab.location['y']
    context.driver.execute_script(f"window.scrollTo({{top: {y_position - 200}, behavior: 'smooth'}});")
    time.sleep(3)