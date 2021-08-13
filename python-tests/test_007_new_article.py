import time


# CON_TC_005_post
# posting a New Article, and testing if it appears
#  calling fixture driver from conftest.py
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
    for i in range(len(tags)):
        assert (tags[i].text == article_tags_list[i])
