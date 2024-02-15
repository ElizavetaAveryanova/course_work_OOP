from abc import ABC, abstractmethod
import json
import os
from config import VACANCY_DIR


class Connector(ABC):
    """Абстрактный класс для работы с файлом вакансий """

    @abstractmethod
    def add_vacancies(self, vacancies) -> None:
        """
        Функция добавляет новые вакансии из переменной vacancies в файл с данными о вакансиях
        """
        pass

    @abstractmethod
    def filter_vacancies(self, search_word) -> list:
        """
        Функция открывает файл с данными о вакансиях, ищет вакансии, содержащие
        поисковое слово search_word и возвращает список отфильтрованных вакансий
        """
        pass

    @abstractmethod
    def top_vacancies(self, top_n) -> list:
        """
        Функция загружает данные о вакансиях из файла, сортирует их по убыванию
        зарплаты и возвращает список с наиболее высокооплачиваемыми вакансиями
        в количестве top_n.
        """
        pass

    @abstractmethod
    def delete_vacancies(self) -> None:
        """Удаляет все вакансии из файла """
        pass


class JsonConnector(Connector):
    """Класс для работы с json-файлом вакансий"""

    file_name = VACANCY_DIR

    def add_vacancies(self, vacancies) -> None:
        """
        Функция добавляет новые вакансии из переменной vacancies в файл с данными
        о вакансиях. Если файл пустой, данные записываются.Если файл не пустой, то данные из
        файла загружаются, затем добавляются новые данные и записываем обновленные данные обратно в файл
        """
        if os.stat(self.file_name).st_size == 0:  # проверяем размер файла, если файл пустой:
            with open(self.file_name, "w", encoding='utf8') as file: # открываем в режиме записи
                json.dump(vacancies, file, indent=2, ensure_ascii=False)  # записываем данные в файл в формате JSON из переменной vacancies

        else:  # иначе, если файл не пустой:
            with open(self.file_name, "r", encoding='utf8') as file: # открываем в режиме чтения
                data = json.load(file)  # выгружаем все данные из файла в переменную data
                data.extend(vacancies)  # добавляем новые данные из переменной vacancies в data
            with open(self.file_name, "w", encoding='utf8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)  # перезаписываем обновленные данные из data в файл

    def filter_vacancies(self, search_word) -> list:
        """
        Функция, которая открывает файл с данными о вакансиях, ищет вакансии, содержащие
        поисковое слово search_word и возвращает список отфильтрованных вакансий
        """
        with open(self.file_name, "r", encoding='utf8') as file:
            data = json.load(file)  # cчитываем данные из файла
            filtered_list = []

            for vacancy in data:  # перебираем вакансии
                for key, value in vacancy.items():
                    if search_word.lower() in str(value).lower():  # ищем соответствия согласно поисковому запросу от пользователя
                        filtered_list.append(vacancy) # добавляем найденную вакансию в список

            return filtered_list

    def top_vacancies(self, top_n) -> list:
        """
        Функция загружает данные о вакансиях из файла, сортирует их по убыванию зарплаты и
        возвращает список с наиболее высокооплачиваемыми вакансиями в количестве top_n
        """

        with open(self.file_name, "r", encoding='utf8') as file:
            data = json.load(file)  # загружаем данные из файла в формате json
            data.sort(key=lambda dictionary: dictionary["salary_from"], reverse=True)  # сортируем по зарплате в порядке убывания

            return data[: top_n]

    def delete_vacancies(self) -> None:
        """
        Функция удаляет все данные из файла с данными о вакансиях, перезаписывая
        его пустым содержимым
        """

        with open(self.file_name, "w", encoding='utf8') as file:
            pass  # перезаписываем файл пустым

# if __name__ == '__main__':
#     connector = JsonConnector()
#
#     vacancies = [{"title": "Develop-разработчик", "salary_from": 170000, "employer": "Газпром", "area": "Уфа"}, {"title": "Тестировщик", "salary_from": 100000, "employer": "Нефтегазсервис", "area": "Казань"}]
#     connector.add_vacancies(vacancies)
#
#     search_word = "Python"
#     filtered_vacancies = connector.filter_vacancies(search_word)
#     print(filtered_vacancies)
#
#     top_n = 2
#     top_vacancies = connector.top_vacancies(top_n)
#     print(top_vacancies)
#
#     connector.delete_vacancies()
