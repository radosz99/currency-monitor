from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import data.connection as db
import data.raport as rap
import data.currency as cur


def get_data(data):
    name = ''
    value = 0
    parts = data.split('td')
    try:
        parts_name = parts[1].split('<')
    except IndexError:
        return
    name = parts_name[0][1:]
    parts_value = parts[5].split('</a>')
    parts_value = parts_value[0].split('>')
    value = parts_value[len(parts_value)-1]
    return name, value

conn = db.get_connection()
current_day = datetime.now().strftime("%Y-%m-%d")
current_hour = datetime.now().strftime("%H:%M")
raport_id = rap.insert_raport(current_day, current_hour, conn)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('resources/chromedriver.exe', options = chrome_options)
driver.get("https://www.x-rates.com/table/?from=PLN&amount=1")
el = driver.find_elements_by_xpath("//tr")
for e in el[1:]:
    try:
        name, value = (get_data(e.get_attribute('innerHTML')))
        value = str(float(value))
    except TypeError:
        continue   
    old_value = cur.insert_currency(raport_id, name, value, conn)
    if old_value is not None:
        if(str(old_value) != value):
            print(f'CHANGE OCCURED | Currency {name}, old - {old_value}, new - {value}')
        else:
            print(f'NO CHANGE | Currency {name}, old - {old_value}, new - {value}')
driver.quit()