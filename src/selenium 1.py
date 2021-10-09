import keyboard
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\91787\PycharmProjects\selenium\driver\chromedriver.exe")
driver.get(r"http://www.greenstechnologys.com/")
driver.maximize_window()
time.sleep(4)
f = driver.find_element(By.XPATH, '//*[@id="article-wrapper"]/p[2]/strong')
m = ActionChains(driver)
m.double_click(f).perform()
m.context_click().perform()
keyboard.press("control + p")
keyboard.release("control + p")


#committed -m "ramu  new commit"