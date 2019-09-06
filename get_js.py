from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://baidu.com")

driver.find_element_by_id("kw").send_keys("aabb")
driver.find_element_by_id("su").click()
driver.quit()
