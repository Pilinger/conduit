import time
import csv
import os


# posting Articles from save_articles.csv
#  calling fixture driver from conftest.py
def test_writing_to_file(driver):
    # assigning test data
    if os.getenv('HEADLESS'):  # if runs on Github
        directory = 'python-tests/test_data/'
    else:  # if runs locally
        directory = 'test_data/'
    filename = 'save_articles.csv'

    time.sleep(1)
    # gathering titles and abouts
    title_elements = driver.find_elements_by_xpath('//div[@class="article-preview"]//h1')
    about_elements = driver.find_elements_by_xpath('//div[@class="article-preview"]//p')
    # generating the list of dictionaries for DictWriter
    list_dict_title_about = []
    for i in range(len(title_elements)):
        sub_dict = {'title': title_elements[i].text, 'about': about_elements[i].text}
        list_dict_title_about.append(sub_dict)

    # assigning the keys, and row count and writing the list into a csv file
    keys_of_list_dict = list_dict_title_about[0].keys()
    row_count = 0
    with open(directory + filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, keys_of_list_dict)
        writer.writeheader()
        for row in list_dict_title_about:
            writer.writerow(row)
            row_count += 1

    # checking if written rows equal to elements count
    assert (row_count == len(title_elements))
