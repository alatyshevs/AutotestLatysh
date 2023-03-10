import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://auto.drom.ru/'
path = os.path.dirname(os.path.realpath(__file__))
parentpath = os.path.abspath(os.path.join(path, os.pardir))
driver = webdriver.Chrome(path + r'\Driver\chromedriver.exe')



def startbrowser(): # Старт Браузера
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Вход')]"))
    )


def login(): # Лигинисмся
    driver.find_element(By.XPATH, "//a[contains(text(),'Вход')]").click()
    driver.find_element(By.XPATH, "// input[ @ name = 'sign']").send_keys('89234092887')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Testov!4545")
    driver.find_element(By.XPATH, "//button[@id='signbutton']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_header_user-info-expand-controller']"))
    )


def search_car(): # Ищем первую попавшуюся машину добоваляем её в избранное
    driver.find_element(By.XPATH,
                        "//div[@class='css-1nvf6xk eqhdpot0']/div/a[contains(@href, 'https')][1]//div[@class='css-cvu2h3 e13r0v7w0']").click()
    driver.implicitly_wait(10)
    driver.get("https://my.drom.ru/personal/bookmark")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='favorites-list_remove-action'][last()]"))
    )
    # Удаляем машину из избранного
    driver.find_element(By.XPATH, "//div[@class='favorites-list_remove-action'][last()]").click()
    driver.implicitly_wait(10)

try:
    startbrowser()
    login()
    search_car()
except Exception:
    print('Errors')
finally:
    print('Ending auto-test')
