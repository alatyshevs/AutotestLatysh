import constants as drom
from tabulate import tabulate
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def startBrowser():
    drom.driver.get(drom.url) #Открываем Браузер переходим на страницу "приморского края"
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@class = 'css-c96isf esqr6ni0']"))
    )
    drom.driver.find_element(By.XPATH, "//a[@class = 'css-c96isf esqr6ni0']").click()
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class = 'b-selectCars__section']"))
    )
    drom.driver.find_element(By.XPATH, drom.input_region('Приморский край')).click()
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Продажа автомобилей в Приморском крае')]"))
    )

def sort_and_transformation(a):
    c = []
    for i in range(len(a)): # убрали из списка последнюю скобку
        c.append(a[i].replace(')', ''))

    delimetr = '('
    mar = []
    for i in range(len(c)): # Используя первую скобку создали вложенные списки
        mar.append(c[i].split(delimetr))
    mar = pd.DataFrame(mar, columns=['a', 'b']) # Сформировали и обозначили колонки таблицы
    mar = mar.astype({'b': np.int32}) # Перевели колонку с количеством в int
    mar = mar.sort_values(by='b', ascending=False) # Выполнили сортировку по Убыванию
    # Для того чтобы иметь 2 колонки в выводе пришлось расформировать по спискам обратно
    mar1 = mar['a'].tolist()
    mar2 = mar['b'].tolist()

    for i in range(len(mar2)):  # Обратно в строковое значение
        mar2[i] = str(mar2[i])

    final = [] # Теперь когда оба списка отсортированы, клеим их обратно беря только верхние 20 элементов добавляем символ " ; " для удобства
    for i in range(20):
        final.append(mar1[i] + '; ' + mar2[i])
    final1 = []
    for i in range(len(final)):
        final1.append(final[i].split(' ; '))
    return final1


def selector():
    WebDriverWait(drom.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, drom.marka_auto_fields))
    )
    drom.driver.find_element(By.XPATH, drom.marka_auto_fields).click()
    # Открываем файл с перечнем всевозможных марок машин
    file = open('catalogAuto.txt', encoding='utf-8')
    A = []
    # перебором собираем весь массив данных
    for i in range(0, 240):
        element = drom.driver.find_element(By.XPATH, drom.marka_auto_fields)
        element.send_keys(file.readline())
        time.sleep(0.2)
        marka = drom.driver.find_elements(By.XPATH, "//div[@class = 'css-1r0zrug e1uu17r80' ]")
        for j in range(0, len(marka)): # Пропускаем : пустые строки, любая марка, машины без объявлений
            if marka[j].text[len(marka[j].text)-1:len(marka[j].text)] == ')':
                A.append(marka[j].text)
        element.clear()
    B = []
    [B.append(x) for x in A if x not in B] # Убираем из списка повторяющиеся элементы
    table = sort_and_transformation(B) # Выполняем сортировку по убыванию и отбрасываем лишнее
    col_names = ['Фирма', 'Количество объявлений'] # Оформляем в виде таблицы
    print(tabulate(table, headers=col_names, tablefmt="grid"))


def runner():
    try:
        startBrowser()
        selector()
    except Exception:
        print('Errors')
    finally:
        print('Ending auto-test')


