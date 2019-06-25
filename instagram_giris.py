from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="D:\Program Files\geckodriver\geckodriver.exe")
browser.get("https://www.instagram.com")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
giris_yap.click()

time.sleep(1)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("user")
password.send_keys("pass")

time.sleep(1)

login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]")
login.click()

time.sleep(7)

browser.close()
