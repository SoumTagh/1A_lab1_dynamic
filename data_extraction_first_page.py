from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import re
import time

# launching the browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)

# waiting for page to load
time.sleep(25)

products = []

# finding all product cards
cards = driver.find_elements(
    By.CSS_SELECTOR,
    'button[data-test^="spotlight-result-product-"]'
)

print(f"Found {len(cards)} products")

for card in cards:
    try:
        # product id
        product_id = card.get_attribute("data-test")
        product_id = product_id.replace("spotlight-result-product-", "")

        # product name
        try:
            name = card.find_element(By.CSS_SELECTOR, "span.text-base").text
        except:
            name = None

        # tagline
        try:
            tagline = card.find_element(By.CSS_SELECTOR, "span.text-sm.font-normal").text
        except:
            tagline = None

        # review count 
        try:
            review_text = card.find_element(By.CSS_SELECTOR, "span.text-sm.font-semibold").text
            review_count = re.search(r"\d+", review_text)
            review_count = review_count.group() if review_count else "0"
        except:
            review_count = "0"

        products.append({
            "id": product_id,
            "name": name,
            "tagline": tagline,
            "review_count": review_count
        })

    except Exception as e:
        print("Error:", e)

# saving into a JSON file
with open("producthunt_first_page.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print(f"{len(products)} products saved.")
driver.quit()