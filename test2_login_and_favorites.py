import time
import constants as drom
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start_browser(): # Старт Браузера
    try:
        drom.logger.info(" # - Старт тест : test2_login_and_favorites.py - # ")
        drom.driver.get(drom.url)
        WebDriverWait(drom.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, drom.authorization))
        )
        drom.logger.info(" ok Браузер запущен успешно ")
    except: 
        drom.logger.exception
        drom.logger.error("! _ Ошибка при открытии браузера _ !")
        raise Exception


def login(): # Логинимся 
    try:    
        drom.driver.find_element(By.XPATH, drom.authorization).click()
        drom.driver.find_element(By.XPATH, drom.login).send_keys('89234092887')
        time.sleep(2)
        drom.driver.find_element(By.XPATH, drom.password).send_keys("Testov!4545")
        drom.driver.find_element(By.XPATH, "//button[@id='signbutton']").click()
        WebDriverWait(drom.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_header_user-info-expand-controller']"))
        )
        drom.logger.info(" ok Авторизация прошла успешно ")
    except:
        drom.logger.exception
        drom.logger.error("! _ Ошибка на форме авторизации _ !")
        raise Exception

def search_car(): # Ищем первую попавшуюся машину добавляем её в избранное
    try:
        drom.driver.find_element(By.XPATH,
                            "//div[@class='css-1nvf6xk eqhdpot0']/div/a[contains(@href, 'https')][1]//div[@class='css-cvu2h3 e13r0v7w0']").click()
        drom.driver.implicitly_wait(10)
        drom.driver.get("https://my.drom.ru/personal/bookmark")
        WebDriverWait(drom.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='favorites-list_remove-action'][last()]"))
        )
        # Удаляем машину из избранного
        drom.driver.find_element(By.XPATH, "//div[@class='favorites-list_remove-action'][last()]").click()
        drom.driver.implicitly_wait(10)
        drom.logger.info(" ok Авто добавлено и удалено из избранного ")
    except:
        drom.logger.exception
        drom.logger.error("! _ Ошибка при добавлении авто в избранное _ !")
        raise Exception


def runner():
    try:
        start_browser()
        login()
        search_car()
    except Exception:
        pass
    finally:
        drom.logger.info(" # - Тест завершён - # ") 

