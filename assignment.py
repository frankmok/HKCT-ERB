from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# Set up the WebDriver (specify the path to your ChromeDriver if not in PATH)
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the Steam Community discussions for Portal 2
    driver.get("https://steamcommunity.com/app/620/discussions/")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".forum_topic_overlay")))

    # Find the fifth thread link (index 4 because it's zero-based)
    threads = driver.find_elements(By.CSS_SELECTOR, ".forum_topic_overlay")
    if len(threads) >= 5:
        fifth_thread = threads[4]
        fifth_thread.click()

        # Wait for the thread page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".commentthread_comment_text")))

        # Find the first post content
        first_post = driver.find_element(By.CSS_SELECTOR, ".commentthread_comment_text")
        post_content = first_post.text

        # Display the content in the terminal
        print("Content of the first post:")
        print(post_content)
    else:
        print("There are not enough threads to select the fifth one.")

finally:
    # Close the browser
    driver.quit()