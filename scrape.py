from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

browser = webdriver.Safari() #driver should be swapped for headless chrome
url = "https://us3.cloud.samsara.com/fleet/viewer/4wl8uKYptOmElqD5Z2ju"
browser.get(url) #navigate to the page

sleep(randint(3,5)) #sleep to allow JS to render page

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

for i in range(0, 7):
    print(browser.execute_script(js, i)) #run JS for every node

browser.quit()
