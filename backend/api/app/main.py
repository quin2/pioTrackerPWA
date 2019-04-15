import json
import sys
from flask import Flask, jsonify, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from time import sleep
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#heuristic: hands on, not abstract

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

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to pioTracker netScrape!"

#detect timeout of browser process and reload it!
@app.route('/api/v0/all', methods=['GET'])
def getBusList():
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    url = "https://us3.cloud.samsara.com/fleet/viewer/4wl8uKYptOmElqD5Z2ju"
    print("browser session starting with id: " + browser.session_id)

    browser.get(url)

    try:
        WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'fleet-map-marker')))
    except TimeoutException as ex:
        print(str(ex))
        browser.close()
        return Response("{Error, please try again}", status=500, mimetype='application/json')

    final = {}
    for i in range(0, 7):
        finalItem = {}
        for j, val in browser.execute_script(js, i):
            finalItem[j] = val
        final[i] = json.dumps(finalItem) #run JS for every node
    browser.close()
    return Response(json.dumps(final), mimetype='application/json')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=80)
