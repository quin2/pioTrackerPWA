from celery import Celery

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json

app = Celery('tasks', broker='amqp://localhost')

js = """
    var item = document.getElementsByClassName('fleet-map-marker')[0].parentNode

    var key = Object.keys(item)[0];
    var finalItem = item[key].memoizedProps.children;
    var loc = finalItem[arguments[0]].props.location;

    var result = [];

    for(var i in loc){
        result.push([i, loc[i]]);
    }
    return result;
"""

@app.task
def fetch():
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    url = "https://us3.cloud.samsara.com/fleet/viewer/4wl8uKYptOmElqD5Z2ju"
    
    browser.get(url)

    try:
        WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'fleet-map-marker')))
    except TimeoutException as ex:
        print(str(ex))
        browser.close()
        return

    final = {}
    for i in range(0, 7):
        finalItem = {}
        for j, val in browser.execute_script(js, i):
            finalItem[j] = val
        final[i] = json.dumps(finalItem) #run JS for every node
    browser.close()
    return json.dumps(final)
