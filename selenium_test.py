from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_duckduckgo_search():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://duckduckgo.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Azure DevOps Selenium")
    search_box.submit()

    time.sleep(2)

    assert "Azure DevOps Selenium" in driver.page_source
    driver.quit()
