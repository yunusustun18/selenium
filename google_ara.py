from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="D:\Program Files\geckodriver\geckodriver.exe")
browser.get("https://www.google.com.tr")

time.sleep(2)

google_ara = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
google_ara.send_keys("siber güvenlik enstitüsü")

ara = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]")
ara.click()

time.sleep(10)

browser.close()
