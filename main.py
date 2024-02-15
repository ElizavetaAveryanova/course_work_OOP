from src.site_api_class import HeadHunterAPI
from src.connector_class import JsonConnector
from src.user_util import user_format


def main():
    # Очищаем файл от предыдущих запусков программы
    json_vac = JsonConnector()
    json_vac.delete_vacancies()

    # Получаем от пользователя ключевое слово для сбора вакансий
    keyword = input("Введите ключевое слово для поиска вакансий: \n")

    json_vac = JsonConnector()

    while True:
        # Пользователь выбирает необходимую команду
        search_way = input("""Выберите команду:
        sort - выдаст вакансии, содержащие ключевое слово
        top - выдаст лучшие вакансии по зарплате \nsort или top: """)

        if search_way not in ("sort", "top"):
            print("Неверная команда")
        else:
            break

    # Собираем файл из вакансий на hh.ru
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(keyword)
    hh_clean_vacancies = hh_api.clean_vacancies(hh_vacancies)
    json_vac.add_vacancies(hh_clean_vacancies)

    # Выводим вакансии по команде сортировки
    if search_way == "sort":
        search_word = input("Введите поисковый запрос для фильтрации вакансий: вакансия/город/зарплата/работодатель \n")
        filtered_vacancies = json_vac.filter_vacancies(search_word)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
        else:
            for vacancy in user_format(filtered_vacancies):
                print(vacancy)

    # Выводим вакансии по команде top
    elif search_way == "top":
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        top_vacancies = json_vac.top_vacancies(top_n)

        if not top_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
        else:
            for vacancy in user_format(top_vacancies):
                print(vacancy)


if __name__ == "__main__":
    main()