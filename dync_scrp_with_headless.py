from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# configuring headless mode
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)

time.sleep(5)

with open("producthunt_raw_with_headless.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Page source saved!")
driver.quit()

"""
here is the output that i got :
Page source saved!
"""