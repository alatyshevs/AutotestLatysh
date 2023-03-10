import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'http://auto.drom.ru/'
path = os.path.dirname(os.path.realpath(__file__))
parentpath = os.path.abspath(os.path.join(path, os.pardir))
driver = webdriver.Chrome(path + r'\Driver\chromedriver.exe')


def filter():
    #Заходим на https://auto.drom.ru/
    driver.get(url)
    driver.implicitly_wait(60)

    # Выбираем марку авто (Toyota)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Марка' ]"))
    )
    driver.find_element(By.XPATH,
                        "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Марка' ]").click()
    driver.find_element(By.XPATH,
                        "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Марка' ]").send_keys('Toyota')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class = 'css-144l089 e1x0dvi10' and contains(text(),'Toyota')]"))
    )
    driver.find_element(By.XPATH,
                        "//div[@class = 'css-144l089 e1x0dvi10' and contains(text(),'Toyota')]").click()

    #Выбираем модель авто (Harrier)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Модель' ]"))
    )
    driver.find_element(By.XPATH,
                        "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Модель' ]").click()
    driver.find_element(By.XPATH,
                        "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Модель' ]").send_keys('Harrier')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class= 'css-10zrduq e140pxhy0']//div[contains(text(),'Harrier') ]"))
    )
    driver.find_element(By.XPATH,
                        "//div[@class= 'css-10zrduq e140pxhy0']//div[contains(text(),'Harrier') ]").click()

    # Выбираем вид топлива (Гибрид)
    driver.find_element(By.XPATH, "//button[contains(text(),'Топливо')]").click()
    driver.find_element(By.XPATH, "//div[@class='css-17vx1of e1x0dvi10' and contains(text() , 'Гибрид')]")

    # Ставим чек бокс (Непроданные)
    driver.find_element(By.XPATH, "//label[@class = 'css-1tikdro eiy4qr62' and contains(text(), 'Непроданные' )]").click()

    # Раскрываем поисковик
    driver.find_element(By.XPATH, "//button[@data-ftid = 'sales__filter_advanced-button' ]").click()

    # Выбираем пробег ( > 1000 )
    driver.find_element(By.XPATH, "//input[@data-ftid ='sales__filter_mileage-from']").send_keys('1000' + Keys.TAB)

    # Выбираем год ( > 2007 )
    driver.find_element(By.XPATH, "//button[contains(text(),'Год')]").click()
    elements = driver.find_elements(By.XPATH, "//div[@class = 'css-17vx1of e1x0dvi10' and contains(text(), '2007')]")
    elements[0].click()

    # Нажимаем кнопку поиска
    driver.find_element(By.XPATH, "//div[@class = 'css-tjza12 e1lm3vns0' and contains(text(), 'Показать')]").click()



def checkFilter():
    headers = driver.find_elements(By.XPATH, "//div[@class='css-1nvf6xk eqhdpot0']/div/a[contains(@href, 'https')]//div[@class= 'css-17lk78h e3f4v4l2']")
    running = driver.find_elements(By.XPATH, "//div[@class =  'css-1fe6w6s e162wx9x0']/span[last() and contains(text(), 'км')]")
    # Если заголовков меньше 20 значит есть проданные авто. Если записей о пробеге меньше 20 значит есть не подержанные авто.
    if len(headers) == 20 and len(running) == 20:
        # Пробегаем по 20 обьявлениям на странице. Смотрим последние 4 символа заголовка. Сверяем их с данными из фильтра.
        for i in range(0, 20):
            year = headers[i].text[len(headers[i].text)-4:len(headers[i].text)]
            if int(year) < 2007:
                raise Exception

    else:
        raise Exception

def checkPages(Quantity):
    i = 0
    while i < Quantity:
        i += 1
        # Просматриваем страницу на совпадение с фильтром.
        checkFilter()
        # Передвигаемся п остраницам выдачи после введения фильтра.
        driver.find_element(By.XPATH, "//a[@class='css-4gbnjj e24vrp30']").click()
    print(Quantity, ' page quality')


try:
    filter()
    checkPages(2)
except Exception as err:
    print('Errors')
finally:
    print('Ending auto-test')

