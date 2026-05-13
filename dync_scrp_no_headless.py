from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# initializing the Chrome browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigating to the url
url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)

# waiting a few seconds for JavaScript to load the content
import time
time.sleep(5)

# saving the page source to a file
with open("producthunt_raw_no_headless.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Page source saved!")

# closing the driver when done
driver.quit()

"""
here is the output that i got :
Page source saved!
"""