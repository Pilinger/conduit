import time


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
