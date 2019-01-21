#!/usr/bin/env python3
from pyvirtualdisplay import Display
from selenium import webdriver
import os, time

display = Display(visible=0, size=(800, 600))
display.start()

router_ip = os.environ["ROUTER_IP"]
admin_pass = os.environ["ADMIN_PASS"]


browser = webdriver.Firefox()
browser.get("http://" + router_ip)
time.sleep(5)
# Type in the password
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[2]/div/div/div[1]/span[2]/input[1]").send_keys(admin_pass)
# Click login
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[3]/div").click()
time.sleep(5)

# Click on button to look at wireless clients
browser.find_element_by_xpath("//*[@id=\"map_icon_wireless\"]").click()
time.sleep(2)

table = browser.find_element_by_css_selector("#map_grid_wireless_host > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1)")
rows = table.find_elements_by_css_selector(".grid-content-tr")
for row in rows:
    ip_addr = row.find_element_by_css_selector(".grid-content-td-ipaddr > .content").get_attribute("textContent")
    mac_addr = row.find_element_by_css_selector(".grid-content-td-macaddr > .content").get_attribute("textContent")
    name = row.find_element_by_css_selector(".grid-content-td-hostname > .content > .name_content_container > .name").get_attribute("textContent")
    print("{}, {}, {}".format(name, ip_addr, mac_addr))

browser.quit()
display.stop()