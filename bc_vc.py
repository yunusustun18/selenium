from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="D:\Program Files\geckodriver\geckodriver.exe")
while(True):
    browser.get("http://bc.vc/y6Ui1ur")

    time.sleep(10)

    reklam_gec = browser.find_element_by_xpath("//*[@id='skip_btt']")
    reklam_gec.click()

    time.sleep(3)