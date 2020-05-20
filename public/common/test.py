from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

dr = webdriver.Chrome()
# dr.get('http://localhost:63342/UItestframework/public/common/test.html')
dr.get('http://192.168.0.223:9002/')
# dr.find_element_by_id('name')
# locate = EC.visibility_of_element_located((By.ID, 'nam1e'))
# ele = WebDriverWait(dr, 10).until(locate)
# print (ele)
