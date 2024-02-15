from src.vacancy_class import Vacancy


def user_format(vacancies: list) -> list[Vacancy]:
    """
    Функция преобразует список словарей с информацией о вакансиях в список
    экземпляров класса Vacancy и возвращает его
    """

    vacancy_cls_list = []
    for vacancy in vacancies:
        vacancy_cls_list.append(Vacancy(vacancy["title"], vacancy["url"], vacancy["salary_from"], vacancy["employer"], vacancy["area"]))

    return vacancy_cls_list

# if __name__ == '__main__':
#     hh_api = Vacancy('разработчик', 'https://', 50000, 'Продакт', 'Казань')
#     print(hh_api)
