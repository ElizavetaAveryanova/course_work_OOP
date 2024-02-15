class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, title, url, salary, employer, area) -> None:
        """ Создание экземпляра класса Vacancy
        :param title: название вакансии
        :param url: ссылка на вакансию url
        :param salary: зарплата
        :param employer: работодатель
        :param area: город
        """
        self.title: str = title
        self.url: str = url
        self.salary: int = salary
        self.employer: str = employer
        self.area: str = area

    def __repr__(self) -> str:
        """ Возвращает информацию об объекте (атрибуты экземпляра) """
        return (f"\nНаименование вакансии: {self.title}\n"
                f"Ссылка на вакансию: {self.url}\n"
                f"Зарплата (от): {self.salary}\n"
                f"Работодатель: {self.employer}\n"
                f"Город: {self.area}\n")

    @staticmethod
    def _is_valid_title(title) -> bool:
        """Проверка названия вакансии """
        return len(title) > 0 and isinstance(title, str)

    @staticmethod
    def _is_valid_url(url) -> bool:
        """Проверка названия ссылки на вакансию """
        return url.startswith("https://") and isinstance(url, str)

    @staticmethod
    def _is_valid_salary(salary) -> bool:
        """Проверка названия зарплаты """
        return isinstance(salary, int)

    @staticmethod
    def _is_valid_employer(employer) -> bool:
        """Проверка названия работодателя """
        return len(employer) > 0 and isinstance(employer, str)

    @staticmethod
    def _is_valid_area(employer) -> bool:
        """Проверка названия города """
        return len(employer) > 0 and isinstance(employer, str)

    def __setattr__(self, key, value):
        """
        Проверка при установке значений атрибутов объектов.
        Если значение атрибута не является исключением, то выполняется установка значений
        """
        if key == "title" and not self._is_valid_title(value):
            raise Exception("Название вакансии не может быть пустым и должно быть строкой")
        if key == "url" and not self._is_valid_url(value):
            raise Exception("Ссылка на вакансию должна быть строкой и начинаться с 'https://'")
        if key == "salary" and not self._is_valid_salary(value):
            raise Exception("Зарплата должна быть числом")
        if key == "employer" and not self._is_valid_employer(value):
            raise Exception("Название работодателя не может быть пустым и должно быть строкой")
        super().__setattr__(key, value)

    def __gt__(self, other) -> bool:
        """Возвращает результат сравнения(>) зарплаты двух вакансий  """
        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        """Возвращает результат сравнения(<) зарплаты двух вакансий """
        return self.salary < other.salary

#
# if __name__ == '__main__':
#     v1 = Vacancy('Разработчик', 'https://', 70000, 'Продакт', 'Уфа')
#     v2 = Vacancy('Тестировщик', 'https://', 55000, 'Телеком', 'Новосибирск')
#
#     print(v1)
#     print(v2)
#     print(v1 > v2)
#     print(v1 < v2)