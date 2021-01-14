from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Ethan/Documents/Bot/chromeDriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

webPage = "https://www.nike.com/nz/launch/t/air-max-95-ndstrkt-neon-yellow"

driver.get(webPage)
print(driver.title)
time.sleep(1)
#main = WebDriverWait(driver, 10).until(
#    EC.presence_of_elements_located(By.ID, "root")
#)

try:
    search = driver.find_element_by_class_name("disabled")
    if search != None:
        print(search.text)
except:
    print("Did not find")

try:
    #Selects size of shoe
    find_size = driver.find_element_by_xpath('//button[contains(text(), "{}")]'.format("10.5"))
    driver.execute_script("arguments[0].scrollIntoView(true);", find_size)
    find_size.click()

    #Adds shoe to cart
    add_cart = driver.find_element_by_xpath('//button[contains(text(), "{}")]'.format("Add to Bag"))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_cart)
    add_cart.click()

    #Checks out cart
    time.sleep(1)
    checkout = driver.find_element_by_xpath('//button[contains(text(), "{}")]'.format("Checkout"))
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout)
    checkout.click()

    #Enters Details into form
    firstName = driver.find_element_by_id("Shipping_FirstName")
    


except:
    print("Error")

#driver.close()