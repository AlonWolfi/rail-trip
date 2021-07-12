import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rail_url = 'https://www.rail.co.il/'

chrome_driver_path = 'chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver_path)
driver.get(rail_url)

# e = driver.find_element_by_class_name('col-md-2 col-sm-5 col-xs-10 fromBox')


try:
    print('Popup - opening')
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ZA_CAMP_DIV_2'))
    )
    print('Popup - closing')
    popup.find_element_by_id('ZA_CANVAS_763351_CLOSE_X2_13_IMG').click()


    print('Waiting for main ...')
    search_main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'trainSearchMain'))
    )


    print('Inserting from station')
    e = search_main.find_element_by_class_name('fromBox')
    e = e.find_element_by_class_name('typeahead')
    from_button = e.find_element_by_tag_name('input')
    from_button.send_keys(TO_STATION)
    from_button.send_keys(Keys.RETURN)


    print('Inserting to station')
    e = search_main.find_element_by_class_name('toBox')
    e = e.find_element_by_class_name('typeahead')
    to_button = e.find_element_by_tag_name('input')
    to_button.send_keys(FROM_STATION)
    to_button.send_keys(Keys.RETURN)


    print('dateTime')
    e = search_main.find_element_by_class_name('dateTimeBox')
    open_date_button = e.find_element_by_tag_name('button')
    open_date_button.click()

    dd = search_main.find_element_by_class_name('displayAndProceed').text.split('\n')[0][:2]
    Month = search_main.find_element_by_class_name('displayAndProceed').text.split('\n')[0][4:].split(',')[0]
    hour = search_main.find_element_by_class_name('displayAndProceed').text.split('\n')[0][4:].split(',')[1][9:]

    # dd = driver.find_element_by_id('legenddatetimefrom').text[11:13]
    # mm = driver.find_element_by_id('legenddatetimefrom').text[14:16]
    # yy = driver.find_element_by_id('legenddatetimefrom').text[17:19]
    # hour = driver.find_element_by_id('legenddatetimefrom').text[27:]

    # close_date_button = search_main.find_element_by_class_name('Calendar-PopUpToCloseBtn')
    # # date_button = e.find_element_by_tag_name('button')
    # close_date_button.click()


except:
    print('Driver failed ...')
    driver.quit()

# ID - trainSearchMain
#

time.sleep(5)

# driver.quit()
