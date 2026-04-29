from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Connexion réussie ! Le titre est :", driver.title)
import time
time.sleep(5)
driver.quit()
