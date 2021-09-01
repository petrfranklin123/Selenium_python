from selenium import webdriver
import time
import random 
#достаем из другого фала данные о пароле
from passs import vk_pass



option = webdriver.ChromeOptions()
driver = webdriver.Chrome()

#если все отработало корректно 
try:
    driver.get("https:/vk.com/")
    #выбираем форму для заполнения 
    email_input = driver.find_element_by_id("index_email")
    #очищаем форму  
    email_input.clear()
    # задействуем нажатие клавиш
    email_input.send_keys("89994765770")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_pass")
    email_input.clear()
    email_input.send_keys(vk_pass)
    time.sleep(5)

    login_buttom = driver.find_element_by_id("index_login_button").click()
    time.sleep(10)

    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)

#обработка исключения 
except Exception as ex:
    print(ex)

#выполняем всегда 
finally:
    driver.close()
    driver.quit()


#if __name__ == "__main__":
#    main()