from time import sleep

from selenium import webdriver


chrome = webdriver.Chrome()

chrome.get("https://www.amazon.com/")


login_page = chrome.find_element_by_xpath("/html/body/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/a[2]")

login_page.click()

sleep(2)

username = chrome.find_element_by_id("ap_email")
username.send_keys("") #your amazon email here

continue_button = chrome.find_element_by_id("continue")
continue_button.click()

password = chrome.find_element_by_id("ap_password")
password.send_keys("") #your amazon password here

signin_button = chrome.find_element_by_id("signInSubmit")
signin_button.click()