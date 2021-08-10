# Generated by Selenium IDE, later modified
import time
# importing web driver waiting components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  calling fixture driver from conftest.py instead

# clicking on decline button and checking if it disappears
def test_decline_cookies(driver):
    time.sleep(1)
    decline_xpath = '//div[@class="cookie__bar__buttons"]/button'
    """Wait or no"""
    decline_buttons = WebDriverWait(driver,
                                    10).until(EC.visibility_of_any_elements_located((By.XPATH, decline_xpath)))
    # decline_buttons = driver.find_elements_by_xpath(decline_xpath)
    assert (len(decline_buttons) > 0)
    decline_buttons[0].click()
    time.sleep(1)
    decline_buttons = driver.find_elements_by_xpath(decline_xpath)
    assert (len(decline_buttons) == 0)


# CON_TC_002_login
# logging in and testing if the username appears correctly
def test_logging_in(driver):
    time.sleep(1)
    # assigning xpath strings, and test strings
    login_xpath = '//a[@href="#/login"]'
    email_xpath = '//input[@placeholder="Email"]'
    password_xpath = '//input[@placeholder="Password"]'
    user_li_xpath = '//*[@id="app"]/nav/div/ul/li[4]/a'
    user_name = 'testuser1'
    password_str = 'Abcd123$'
    email_end = '@example.com'
    """Wait or no"""
    login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_xpath)))
    # login = driver.find_element_by_xpath(login_xpath)
    login.click()
    time.sleep(1)
    driver.find_element_by_xpath(email_xpath).send_keys(f'{user_name}{email_end}')
    time.sleep(1)
    driver.find_element_by_xpath(password_xpath).send_keys(password_str)
    time.sleep(1)
    driver.find_element_by_xpath('//form/button').click()
    time.sleep(2)
    username = driver.find_element_by_xpath(user_li_xpath).text
    assert (username == user_name)


# paginating through the pages, and testing if its possible
def test_paginate(driver):
    # collecting the clickable pagination links
    paginate_links = driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
    assert (len(paginate_links) > 0)
    for link in paginate_links:
        link.click()
        time.sleep(1)


# CON_TC_005_post
# posting a New Article, and testing if it appears
def test_new_article(driver):
    # data for posting
    article_title_str = 'This is a test article.'
    article_about_str = 'This is about to test the posting method.'
    article_markdown_str = "I'm about to test the posting method of the conduit site."
    article_tags_list = ['test', 'post']
    # clicking the New Article button
    new_article_xpath = '//a[@href="#/editor"]'
    driver.find_element_by_xpath(new_article_xpath).click()
    time.sleep(2)
    # gathering the inputs and buttons
    title_input = driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]')
    about_input = driver.find_element_by_xpath('//input[@class="form-control"]')
    text_input = driver.find_element_by_xpath('//textarea')
    tags_input = driver.find_element_by_xpath('//input[@class="ti-new-tag-input ti-valid"]')
    publish_article_button = driver.find_element_by_tag_name('button')

    # assigning values to the inputs, and publishing the Article
    title_input.send_keys(article_title_str)
    time.sleep(1)
    about_input.send_keys(article_about_str)
    time.sleep(1)
    text_input.send_keys(article_markdown_str)
    time.sleep(1)
    tags_input.send_keys(f'{article_tags_list[0]},{article_tags_list[1]}')
    time.sleep(1)
    publish_article_button.click()
    time.sleep(1)

    # checking the strings to a newly posted Article
    assert (article_title_str == driver.find_element_by_tag_name('h1').text)
    assert (article_markdown_str == driver.find_element_by_tag_name('p').text)
    tags = driver.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
    assert (tags[0].text == article_tags_list[0])
    assert (tags[1].text == article_tags_list[1])


# CON_TC_007_edit
# Editing the newly posted Article
def test_editing(driver):
    def get_textarea():
        return driver.find_element_by_tag_name('textarea')

    # data for editing
    plus_str = ' And now its edited too.'
    # gathering the button and clicking it
    edit_button = driver.find_element_by_xpath('//a[@class="btn btn-sm btn-outline-secondary"]')
    time.sleep(1)
    edit_button.click()
    time.sleep(2)
    # gathering the input and button
    edit_field = get_textarea()
    publish_button = driver.find_element_by_tag_name('button')
    # assigning string, and click the publish button
    edit_field.send_keys(plus_str)
    edit_field = get_textarea()
    edited_text = edit_field.get_attribute('value')
    time.sleep(1)
    publish_button.click()
    time.sleep(2)
    # checking if the edited text appears correctly
    assert (edited_text == driver.find_element_by_tag_name('p').text)


# CON_TC_008_delete
# deleting the Newly Edited Article
def test_delete(driver):
    def get_headers():
        return driver.find_elements_by_xpath('//div[@class="article-preview"]/a/h1')

    def checking_page():
        headers = get_headers()
        for header in headers:
            assert (header.text != article_title)

    # gathering the article title and delete button and deleting the article
    article_title = driver.find_element_by_tag_name('h1').text
    delete_button = driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]')
    delete_button.click()
    time.sleep(2)
    # collecting the clickable pagination links
    paginate_links = driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
    for link in paginate_links:
        link.click()
        time.sleep(1)
        # searching the articles by title to check the article was deleted
        checking_page()
