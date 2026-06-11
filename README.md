# 1A_lab1_dynamic

### Dynamic Web Scraping
I installed Selenium and webdriver-manager to control a real Chrome browser, navigated to ProductHunt search results for "mental health ai", then i tested both headless and non-headless modes:
  - Without headless : a visible Chrome window opens and navigates
  - With headless : everything runs invisibly in the background, faster and lighter
  
Using Selenium, I automated the extraction of product information from the first page of Product Hunt search results for the query "mental health ai". The scraper collected the product ID, product name, tagline, and review count for each product card. For missing fields (review counts of some products for instance) were handled gracefully through individual try/except blocks to ensure robust execution. Finally, the extracted data was first saved to a JSON file and then converted into a CSV file for easier analysis and further processing.

I attempted to extend the scraper beyond the first search results page in order to scrape data from the rest of the pages, but the attempts were blocked by Cloudflare. Navigating to subsequent pages triggered a bot-detection challenge, preventing the scraper from collecting additional search results. Similarly, opening individual product pages to extract more detailed information also activated Cloudflare protection, blocking access to the page content. Therefore, while the scraping logic for pagination and product-detail extraction can be implemented, Cloudflare's anti-bot measures prevent their execution in practice without the use of specialized anti-bot bypass solutions.
