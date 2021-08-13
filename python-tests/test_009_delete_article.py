import time


# CON_TC_008_delete
# deleting the Newly Edited Article
#  calling fixture driver from conftest.py
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
