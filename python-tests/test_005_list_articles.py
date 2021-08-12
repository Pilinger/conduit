def test_list_articles(driver):
    # after logging in, the Global Feed automatically lists the Articles
    articles = driver.find_elements_by_class_name('article-preview')
    assert (len(articles) > 0)
