import json
import sys
from flask import Flask, jsonify, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from random import randint

js = """
    var item = document.getElementsByClassName('fleet-map-marker')[0].parentNode

    var key = Object.keys(item)[0];
    var finalItem = item[key].memoizedProps.children;
    var loc = finalItem[arguments[0]].props.location;

    var result = [];
        for(var i in loc)
        result.push([i, loc[i]]);
    return result;
"""

app = Flask(__name__)

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

@app.before_first_request
def busLoader():
    url = "https://us3.cloud.samsara.com/fleet/viewer/4wl8uKYptOmElqD5Z2ju"
    browser.get(url)
    sleep(randint(3,5))

@app.route('/')
def index():
    return "Welcome to pioTracker netScrape!"

#new bug: will only give good response ONCE!
@app.route('/api/v0/all', methods=['GET'])
def getBusList():
    final = {}
    for i in range(0, 7):
        finalItem = {}
        for j, val in browser.execute_script(js, i):
            finalItem[j] = val
        final[i] = json.dumps(finalItem) #run JS for every node
    return Response(json.dumps(final), mimetype='application/json')

if __name__ == '__main__':
    app.run()
    browser.quit()
