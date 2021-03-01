from config import mysql


class EmployeeModel(object):

    @staticmethod
    def get_employees_by_dep(id: int) -> list:
        # Формируем список и параметризированный запрос (защищенный)
        emp_list = []
        query = 'select * from employees where dep_id=%s'
        cursor = mysql.get_db().cursor()
        cursor.execute(query, (id,))

        for row in cursor.fetchall():
            emp_list.append({
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'position': row[3],
                'salary': row[4],
                'dep_id': row[5]
            })
        return emp_list

    @staticmethod
    def add_employee(name, age, position, salary, dep_id) -> None:
        query = 'insert into employees (name, age, position, salary, dep_id) values (%s, %s, %s, %s, %s)'
        connection = mysql.get_db()
        cursor = connection.cursor()
        cursor.execute(query, (name, age, position, salary, dep_id))
        connection.commit()
