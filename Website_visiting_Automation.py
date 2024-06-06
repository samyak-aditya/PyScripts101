import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def visit_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Visited {url} successfully.")
        else:
            print(f"Failed to visit {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def open_browser_and_scroll(url):
    options = Options()
    options.add_argument("--headless")  # Run headless if you don't want to see the browser window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Scroll to the end of the page
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        print(f"Scrolled to the end of {url}")

        # Wait for 10 seconds
        time.sleep(10)
    finally:
        driver.quit()

def auto_visit_webpage(url, interval, repetitions):
    for _ in range(repetitions):
        visit_webpage(url)
        open_browser_and_scroll(url)
        time.sleep(interval)

if __name__ == "__main__":
    # Configuration
    url = "https://www.example.com"   # Replace with your target URL
    interval = 15  # Time interval in seconds
    repetitions = 20  # Number of times to visit the webpage

    auto_visit_webpage(url, interval, repetitions)
    
