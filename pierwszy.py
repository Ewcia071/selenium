#Import bibliotek
from selenium import webdriver
from time import sleep



#Tworzymy obiekt
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.wsb.pl')
#spij 5 sekund
sleep(5)
driver.quit()
