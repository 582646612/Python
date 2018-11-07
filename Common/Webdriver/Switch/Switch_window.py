from selenium import  webdriver
import  time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
sreach_windows=driver.current_window_handle#获取当前句柄
print (sreach_windows)
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
the_windows=driver.current_window_handle#driver.window_handles获取所有句柄
print (the_windows)
time.sleep(3)
driver.switch_to_window(sreach_windows)
time.sleep(2)
driver.switch_to_window(the_windows)
# time.sleep(2)
# driver.switch_to_window(sreach_windows)
# time.sleep(2)
# driver.switch_to_window(all_handles)
# time.sleep(2)2
#driver.quit()
