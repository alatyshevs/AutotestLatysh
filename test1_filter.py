import constants as drom
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def filter():
    #Заходим на https://auto.drom.ru/
    drom.driver.get(drom.url)
    drom.driver.implicitly_wait(60)

    # Выбираем марку авто (Toyota)
    marka_auto = 'Toyota'
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, drom.marka_auto_fields))
    )
    drom.driver.find_element(By.XPATH, drom.marka_auto_fields).click()
    drom.driver.find_element(By.XPATH, drom.marka_auto_fields).send_keys(marka_auto)
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, drom.input_marka_auto(marka_auto)))
    )
    drom.driver.find_element(By.XPATH, drom.input_marka_auto(marka_auto)).click()

    #Выбираем модель авто (Harrier)
    model_auto = 'Harrier'
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, drom.model_auto_fields))
    )
    drom.driver.find_element(By.XPATH, drom.model_auto_fields).click()
    drom.driver.find_element(By.XPATH, drom.model_auto_fields).send_keys(model_auto)
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, drom.input_model_auto(model_auto)))
    )
    drom.driver.find_element(By.XPATH, drom.input_model_auto(model_auto)).click()

    # Выбираем вид топлива (Гибрид)
    fuel = 'Гибрид'
    drom.driver.find_element(By.XPATH, drom.fuel_fields).click()
    drom.driver.find_element(By.XPATH, drom.input_fuel(fuel)).click()

    # Ставим чек бокс (Непроданные)
    drom.driver.find_element(By.XPATH, drom.input_check_box('Непроданные')).click()

    # Раскрываем поисковик
    drom.driver.find_element(By.XPATH, drom.advanced_search).click()

    # Выбираем пробег ( > 1 кт )
    drom.driver.find_element(By.XPATH, drom.run_more_than).send_keys('1' + Keys.TAB)

    # Выбираем год ( >= 2007 )
    drom.driver.find_element(By.XPATH, drom.year_more_than).click()
    elements = drom.driver.find_elements(By.XPATH, drom.input_year_more_than('2007'))
    elements[0].click()

    # Нажимаем кнопку поиска
    drom.driver.find_element(By.XPATH, drom.search_filter).click()


def checkFilter():
    headers = drom.driver.find_elements(By.XPATH, "//div[@class='css-1nvf6xk eqhdpot0']/div/a[contains(@href, 'https')]//div[@class= 'css-17lk78h e3f4v4l2']")
    running = drom.driver.find_elements(By.XPATH, "//div[@class =  'css-1fe6w6s e162wx9x0']/span[last() and contains(text(), 'км')]")
    # Если заголовков меньше 20 значит есть проданные авто. Если записей о пробеге меньше 20 значит есть не подержанные авто.
    if len(headers) == 20 and len(running) == 20:
        # Пробегаем по 20 объявлениям на странице. Смотрим последние 4 символа заголовка. Сверяем их с данными из фильтра.
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
        # Передвигаемся по страницам выдачи после введения фильтра.
        drom.driver.find_element(By.XPATH, drom.button_next).click()
    print(Quantity, ' page quality')


def runner():
    try:
        filter()
        checkPages(2)
    except Exception as err:
        print('Errors')
    finally:
        print('Ending auto-test')



