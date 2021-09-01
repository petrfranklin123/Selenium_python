from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from model import Question
from time import sleep, ctime, time

class ProgHubParser(object):
    #конструктор класса
    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang
    #метод вызова парсера
    def parse(self):
        self.go_to_tests_page()
        self.parse_question_page()
    #https://selenium-python.readthedocs.io/locating-elements.html

    def go_to_tests_page(self):
        self.driver.get("https://proghub.ru/tests")
        #получаем коллекцию с тегом а
        slide_elems = self.driver.find_elements_by_tag_name("a")

        for elem in slide_elems:
            #получаем атрибут
            lang_link = elem.get_attribute("href")
            #проверяем, есть ли строка с python-3-basic в выбранных ссылках
            if  self.lang in lang_link:
                #Сплитуем и берем последний, то есть python-3-basic и переходим по сформированной ссылке
                language = lang_link.split("/")[-1]
                self.driver.get("https://proghub.ru/t/" + language)
                
                #выделяем ссылку кнопки "Пример" и переходим по ней на тест
                link_test = self.driver.find_element_by_css_selector(".btn-cyan")
                self.driver.get(link_test.get_attribute("href"))

                break
    
    #Функция записи значений в объект
    def parse_question_page(self):
        #создаем объект
        questions = Question()
        #Вызываем нижнюю функцию 
        self.fill_questions_text(questions)

        self.fill_questions_code(questions)

        self.fill_questions_answers(questions)
        #выводим весь класс 
        print(questions)

    #Функция парсинга теста 
    def fill_questions_text(self, question):
        # Если был поменянн тег или путь, ообработка исключения 
        try:
            # Ведем поиск по css
            question_test_elm = self.driver.find_element_by_css_selector("h1")
            # Записываем в объект 
            question.text = question_test_elm.text
        #Прописываем название ошибки 
        except NoSuchElementException:
            print("Что-то пошло не так... Пути такого не наблюдаю")

    def fill_questions_code(self, question):
        # Если был поменянн тег или путь, ообработка исключения 
        try:
            # Ведем поиск по css
            code_elm = self.driver.find_element_by_css_selector("code")
            # Записываем в объект 
            question.code = code_elm.text
        #Прописываем название ошибки 
        except NoSuchElementException:
            print("Что-то пошло не так... Пути такого не наблюдаю или кода в задании просто нет")


    def fill_questions_answers(self, questions):
        btn_answer = self.driver.find_element_by_css_selector(".answer")
        btn_answer.click()

        sleep(1)
        btn_answer = self.driver.find_element_by_css_selector(".btn-primary")
        btn_answer.click()

        sleep(4)

        answer_elems = self.driver.find_elements_by_css_selector(".answer")
        for answer_elem in answer_elems:
            answer = [answer_elem.text, False]

            
            #test = answer.get_attribute('class').split(' ')[-1]
            
            #print(test)

            if 'correct' == answer_elem.get_attribute('class').split(' ')[-1]:
                answer[1] = True
            
            questions.answers.append(answer)
            



def main():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, "python-3-basic")
    parser.parse()
    #driver.get("https://proghub.ru/developer")
    #btn_elem = driver.find_element_by_class_name("menu_item")
    #btn_elem.click()

    #titleh2 = driver.find_element_by_tag_name("h2")
    #print(titleh2.text)

    sleep(40)
    

if __name__ == "__main__":
    main()
