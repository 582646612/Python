#
# js="var q=document.getElementById('id').scrollTop=10000"
# driver.execute_script(js）
#
#
# target = driver.find_element_by_id("id_keypair")
# driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
#
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_id("id_login_method_0").send_keys(Keys.TAB)