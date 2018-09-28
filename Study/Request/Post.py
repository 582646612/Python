from selenium import webdriver
# Simple usage with built-in WebDrivers:
driver = webdriver.Firefox()
response = driver.request('GET', 'https://www.baidu.com/')
print(response)
driver.close()