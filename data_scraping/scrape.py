import os
import sys
import urllib.request
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

# Specify the path to chromedriver.exe  --> using WSL :)
chrome_driver_path = 'D:\\per\\softwares\\chromedriver-win64\\chromedriver.exe'
# chrome_driver_path = '/mnt/d/per/softwares/chromedriver-win64/chromedriver.exe'

# Initialize the selenium web driver
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()


# https://stackoverflow.com/a/76599068
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.set_capability("cloud:options", {"name": "test_1"})
driver = webdriver.Chrome(service=service, options=options)



query = sys.argv[1]
query = query.split()
query = '+'.join(query)
url = "http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

# Add the directory for your image here
DIR = "Pictures"

driver.get(url)

# Simulate scrolling down to load more images (adjust the number of scrolls as needed)
num_scrolls = 100
# print(f"drivers methods: {dir(driver)}")   #checking all of the driver methods
for _ in range(num_scrolls):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(5)  # wait for 5 sec when finding elements on the page,
                               # before throwing an exception

soup = BeautifulSoup(driver.page_source, "html.parser")

# Use regular expressions to find image URLs in the HTML source code
image_urls = re.findall(r'"murl":"(.*?)"', str(soup))

if not os.path.exists(DIR):
    os.mkdir(DIR)

DIR = os.path.join(DIR, query.split()[0])
if not os.path.exists(DIR):
    os.mkdir(DIR)

# Download images
for i, img_url in enumerate(image_urls):
    try:
        image_name = img_url.split("/")[-1]
        raw_img = urllib.request.urlopen(img_url).read()

        cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1

        f = open(os.path.join(DIR, image_name), 'wb')
        f.write(raw_img)
        f.close()
        print(f"Downloaded image {cntr}: {image_name}")
    except Exception as e:
        print(f"Could not load: {img_url}")
        print(e)

print("Data scraping and image downloading completed.")

# Close the web driver when done
driver.close()
