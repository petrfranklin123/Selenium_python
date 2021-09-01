#программа отключения webdriver 

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#import random 
from selenium.webdriver.common.keys import Keys
#ожидание подгркзки элементов 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#достаем из другого фала данные о пароле
from passs import vk_pass



option = webdriver.ChromeOptions()

#для старых браузеров
#option.add_experimental_option("excludeSwitches", ["enable-automation"])
#option.add_experimental_option("useAutomationExtension", False)

#для новых браузеров 
option.add_argument("--disable-blink-features=AutomationControlled")

#фоновый режим 
#option.add_argument("--headless")
#option.headless = True

driver = webdriver.Chrome(options=option)

def waitCSS(driver, search):
    return WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(search))

def waitXPATHs(driver, search):
    return WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath(search))

#если все отработало корректно 
try:
    #ссылка на просмотр данных об режиме браузера 
    driver.get("https://www.avito.ru/")

    #wait = WebDriverWait(driver, 10)
    #search = wait.until(EC.element_to_be_selected(By.ID, "search"))

    #search = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID("search")))

    #time.sleep(2)
    #search = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("search"))

    search = waitCSS(driver, "#search")

    #search = driver.find_element_by_id("search")

    #количество открытых вкладок 
    print(driver.window_handles)
    #url текущей вкладки
    print(f"URL is : {driver.current_url}")

    search.send_keys("Видеокарты")
    search.send_keys(Keys.ENTER)
    #time.sleep(3)

    #количество открытых вкладок 
    print(driver.window_handles)
    #url текущей вкладки
    print(f"URL is : {driver.current_url}")

    #получаем список из объявлений
    #items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items = waitXPATHs(driver, "//div[@data-marker='item-photo']")
    items[0].click()

    #time.sleep(3)
    #обязательно делаем переход, иначе мы будем, формально, на прошлой странице
    driver.switch_to.window(driver.window_handles[1])

    #количество открытых вкладок 
    print(driver.window_handles)
    #url текущей вкладки
    print(f"URL is : {driver.current_url}")

    #получаем имя владельца поста 
    user_name = waitCSS(driver, ".seller-info-name")
    print(f"User is name : {user_name.text}")
    #time.sleep(3)

    #закрываем открытое окно 
    driver.close()

    #чтобы не возникло ошибок, переходим на первую вкладку 
    driver.switch_to.window(driver.window_handles[0])
    #time.sleep(3)
    print(f"URL is : {driver.current_url}")


    #заходим на новую вкладку 
    items[1].click()
    #обязательно делаем переход, иначе мы будем, формально, на прошлой странице
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    user_name = driver.find_element_by_xpath("//div[@data-marker='seller-info/name']")
    print(f"User is name : {user_name.text}")

    ad_date = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"An ad date is : {ad_date.text}")

    joined_date = driver.find_element_by_class_name("seller-info-value")
    print(f"User since : {joined_date.text}")

    '''
    #переход на первую вкладку
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    items[1].click()
    #количество открытых вкладок 
    print(driver.window_handles)
    #url текущей вкладки
    print(f"URL is : {driver.current_url}")
    time.sleep(5)
    '''


#обработка исключения 
except Exception as ex:
    print(ex)

#выполняем всегда 
finally:
    driver.close()
    driver.quit()


#if __name__ == "__main__":
#    main()