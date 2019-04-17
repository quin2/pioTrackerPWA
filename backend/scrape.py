import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from random import randint

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
url = "https://us3.cloud.samsara.com/fleet/viewer/4wl8uKYptOmElqD5Z2ju"
browser.get(url) #navigate to the page

sleep(randint(3,5)) #sleep to allow JS to render page

def runall():
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
    final = {}

    for i in range(0, 7):
        finalItem = {}
        for j, val in browser.execute_script(js, i):
            finalItem[j] = val
        final[i] = finalItem #run JS for every node

    print(final)

runall()
runall()


#need to 'hydrate' array into JSON
#and send JSON over flask or similar

browser.quit()
