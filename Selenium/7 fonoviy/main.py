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

#фоновый режим 
#option.add_argument("--headless")
option.headless = True

driver = webdriver.Chrome(options=option)

#если все отработало корректно 
try:
    #ссылка на просмотр данных об режиме браузера 
    driver.get("http://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(3)

    print("завершение проверки")

    driver.get("https:/vk.com/")
    #выбираем форму для заполнения 
    email_input = driver.find_element_by_id("index_email")
    #очищаем форму  
    email_input.clear()
    # задействуем нажатие клавиш
    email_input.send_keys("89994765770")
    time.sleep(3)

    print("вставка номера телефона")

    email_input = driver.find_element_by_id("index_pass")
    email_input.clear()
    email_input.send_keys(vk_pass)
    time.sleep(3)

    print("вставка пароля")


#обработка исключения 
except Exception as ex:
    print(ex)

#выполняем всегда 
finally:
    driver.close()
    driver.quit()


#if __name__ == "__main__":
#    main()