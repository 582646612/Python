def scroll(driver):
    target = driver.find_element_by_name("日期和时间")
    driver.execute_script("arguments[0].scrollIntoView();", target)