from selenium import webdriver
import time
import random 

#url = "https://www.instagram.com/" 
#внутри chrome записывается путь драйвера executable_path="..."

user_agent_list = [
    "hello_world",
    "best",
    "python"
]

option = webdriver.ChromeOptions()
#изменяем user-agent
#option.add_argument("user-agent=Hello_World")
#рандомно выдергиваем список 
option.add_argument(f"user-agent={random.choice(user_agent_list)}")


#driver = webdriver.Chrome()
#применяем новый user-agent
#таким образом мы можем эмулировать работу любого устройства на сайте
#user-agent любого устройства можно найти в интернете 
driver = webdriver.Chrome(options=option)

#если все отработало корректно ы
try:

    driver.get("https://xn--80agecg4bru4h.xn--p1ai/")

    #driver.get(url)
    time.sleep(5)
    #сделать скриншот 
    #driver.get_screenshot_as_file("1.png")

#обработка исключения 
except Exception as ex:
    print(ex)

#выполняем всегда 
finally:
    driver.close()
    driver.quit()


#if __name__ == "__main__":
#    main()