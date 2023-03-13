import os
from selenium import webdriver
from loguru import logger



url = 'http://auto.drom.ru/'
path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(path + r'\Driver\chromedriver.exe')
logger.add("debug.log", format="{time:YYYY:MMM:D:HH:mm:Z} {level} {message}",
           level="DEBUG", rotation="200 MB",  compression="zip")


# XPATH FILTER FIELDS
# Marka auto 
marka_auto_fields = "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Марка' ]"
# Model auto 
model_auto_fields = "//div[@class = 'css-75hx9m e1a8pcii0']//input[@placeholder = 'Модель' ]"
# Fuel
fuel_fields = "//button[contains(text(),'Топливо')]"
# Button Advanced Search
advanced_search = "//button[@data-ftid = 'sales__filter_advanced-button' ]"
# Mileage more than
run_more_than = "//input[@data-ftid ='sales__filter_mileage-from']"
# A year more than
year_more_than = "//button[contains(text(),'Год')]"
# Filter search
search_filter = "//div[@class = 'css-tjza12 e1lm3vns0' and contains(text(), 'Показать')]"
# Button next
button_next = "//a[@class='css-4gbnjj e24vrp30']"
# Choose regions
region = "//a[@class = 'b-link regionLink' and contains(text(), 'Приморский край')]"
# Login
login = "// input[ @name = 'sign' ]"
# Password 
password = "//input[ @name = 'password' ]"
# Button authorization
authorization = "//a[contains(text(),'Вход')]"



# XPATH POP-UP FILTER
def input_marka_auto(marka_auto):
    return "//div[@class = 'css-144l089 e1x0dvi10' and contains(text(), '" + marka_auto + "')]"

def input_model_auto(model_auto):
    return "//div[@class= 'css-10zrduq e140pxhy0']//div[contains(text(), '" + model_auto + "') ]"

def input_fuel(fuel):
    return "//div[@class='css-17vx1of e1x0dvi10' and contains(text() , '" + fuel + "')]"

def input_check_box(box):
    return "//label[@class = 'css-1tikdro eiy4qr62' and contains(text(), '" + box + "' )]"

def input_year_more_than(year):
    return "//div[@class = 'css-17vx1of e1x0dvi10' and contains(text(), '" + year + "')]"

def input_region(region):
    return "//a[@class = 'b-link regionLink' and contains(text(), '" + region + "')]"
