import time


# paginating through the pages, and testing if its possible
def test_paginate(driver):
    # collecting the clickable pagination links
    paginate_links = driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
    assert (len(paginate_links) > 0)
    for link in paginate_links:
        link.click()
        time.sleep(1)
