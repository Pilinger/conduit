import time
import csv
import os


# posting Articles from new_articles.csv
#  calling fixture driver from conftest.py
def test_posting_from_file(driver):
    def clear_and_send_keys(element, string):
        element.clear()
        time.sleep(1)
        element.send_keys(string)
        time.sleep(1)

    def post_article(title, about, text, tags):
        driver.find_element_by_xpath(new_article_xpath).click()
        time.sleep(1)
        # gathering the inputs and buttons
        title_input = driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]')
        about_input = driver.find_element_by_xpath('//input[@class="form-control"]')
        text_input = driver.find_element_by_xpath('//textarea')
        tags_input = driver.find_element_by_xpath('//input[@class="ti-new-tag-input ti-valid"]')
        publish_article_button = driver.find_element_by_tag_name('button')
        # assigning values to the inputs, and publishing the Article
        clear_and_send_keys(title_input, title)
        clear_and_send_keys(about_input, about)
        clear_and_send_keys(text_input, text)
        clear_and_send_keys(tags_input, tags)
        publish_article_button.click()
        time.sleep(1)

    def check_article(title, about, text, tag):
        assert (title == driver.find_element_by_tag_name('h1').text)
        assert (text == driver.find_element_by_tag_name('p').text)
        tags = driver.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
        for i in range(len(tags)):
            assert (tags[i].text == tag)

    # assigning test data
    if os.getenv('HEADLESS'):  # if runs on Github
        directory = 'python-tests/test_data'
    else:  # if runs locally
        directory = 'test_data/'
    filename = 'new_articles.csv'
    new_article_xpath = '//a[@href="#/editor"]'

    with open(directory + filename, 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            post_article(row['title'], row['about'], row['text'], row['tags'])
            check_article(row['title'], row['about'], row['text'], row['tags'])
