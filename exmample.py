emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 100000)


def insert_emp(emp):
  with conn: #for insert, update, remove use with conn:
    cursor.execute("INSERT INTO voitures VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, ...)

                                                                       
def get_emp_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last=: lastname})
    return cursor.fetchall
               
