from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(price_dollar.text + "." + price_cents.text)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# print(documentation_link.get_attribute("href"))

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# print(bug_link.get_attribute("href"))

upcoming_events_list = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last ul li")
update_events = {
    event.find_element(By.CLASS_NAME, value="say-no-more").text:event.find_element(By.TAG_NAME, 'a').text for event in upcoming_events_list
}

print(update_events)

# Close the browser
# driver.close()
driver.quit()
