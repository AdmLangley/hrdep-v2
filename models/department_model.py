from config import mysql


class DepartmentModel(object):

    @staticmethod
    def get_all_departments() -> list:
        dep_list = []
        # Здесь сценарий извлечения данных и заполнения dep_list
        # Курсор необходим для работы с данными в БД
        cursor = mysql.get_db().cursor()

        # Вызываем метод в курсоре, который передает SQL команду и записывает в кэш полученные данные
        cursor.execute('SELECT * FROM departments ORDER by id')

        # Из кеша теперь надо построчно извлекать данные
        for row in cursor.fetchall():
            dep_list.append({
                'id': row[0],
                'name': row[1]
            })
        return dep_list


    @staticmethod
    def get_depname_by_id(id: int) -> str:
        query = 'select name from departments where id=%s'
        cursor = mysql.get_db().cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        return row[0]


    @staticmethod
    def get_employees() -> list:
        employees_list = []
        # Здесь будет камбек списка юзеров
        return employees_list
