#программа отключения webdriver 

from selenium import webdriver
import time
import random 
#достаем из другого фала данные о пароле
from passs import vk_pass



option = webdriver.ChromeOptions()

#для старых браузеров
#option.add_experimental_option("excludeSwitches", ["enable-automation"])
#option.add_experimental_option("useAutomationExtension", False)

#для новых браузеров 
option.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=option)

#если все отработало корректно 
try:
    #ссылка на просмотр данных об режиме браузера 
    driver.get("http://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

#обработка исключения 
except Exception as ex:
    print(ex)

#выполняем всегда 
finally:
    driver.close()
    driver.quit()


#if __name__ == "__main__":
#    main()