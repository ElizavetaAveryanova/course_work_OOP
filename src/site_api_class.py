from abc import ABC, abstractmethod
import requests


class HHSiteAPI(ABC):
    """
    Абстрактный класс для работы с API сайта hh.ru
    """

    @abstractmethod
    def get_vacancies(self, keyword) -> dict:
        """
        Возвращает отфильтрованные по ключевому слову keyword вакансии с сайта
        """
        pass

    @staticmethod
    def clean_vacancies(data) -> list:
        """Создание списка с информацией о вакансиях"""
        pass

class HeadHunterAPI(HHSiteAPI):
    """Класс для работы с API сайта с вакансиями hh.ru"""

    def __init__(self):
        """Создание экземпляра класса HeadHunterAPI"""
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword) -> dict:
        """
        Функция выполняет запрос на получение данных о вакансиях с помощью
        ключевого слова keyword и возвращает полученные данные в формате словаря.
        Если запрос не удался, то вызывается исключение.
        """
        params = {
            "text": keyword,  # ключевое слово фильтра
            "area": 113,  # страна для поиска работы (Россия)
            "per_page": 100,  # количество вакансий
        }
        response = requests.get(self.url, params=params) # отправляем get-запрос
        if response.status_code == 200:
            data = response.json() # сохраняем данные из ответа в формате json
            return data
        else:
            raise Exception(f"Запрос не выполнен: {response.status_code}")

    @staticmethod
    def clean_vacancies(data) -> list:
        """
        Функция, которая принимает словарь с данными о вакансиях, обрабатывает и создает список
        с информацией о вакансиях (название вакансии, URL, зарплата, работодатель, город)
        """
        clean_vacancies = []
        vacancies = data.get("items", []) # получаем список вакансий из словаря data, если ключ "items" отсутствует, то []
        for vacancy in vacancies: # перебираем список vacancies
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            try:
                vacancy_salary_from = vacancy.get("salary", {}).get("from")
                if vacancy_salary_from is None:
                    vacancy_salary_from = 0
            except AttributeError:
                vacancy_salary_from = 0
            vacancy_employer = vacancy.get("employer", {}).get("name")
            vacancy_area = vacancy.get("area", {}).get("name")

            clean_vacancies.append({"title": vacancy_title,
                                    "url": vacancy_url,
                                    "salary_from": vacancy_salary_from,
                                    "employer": vacancy_employer,
                                    "area": vacancy_area})

        return clean_vacancies # возвращаем список словарей с данными о вакансиях


# if __name__ == '__main__':
#     hh_api = HeadHunterAPI()
#     data = hh_api.get_vacancies('разработчик')
#     print(data)
#     print(hh_api.clean_vacancies(data))