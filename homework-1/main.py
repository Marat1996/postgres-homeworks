import csv
import psycopg2

# Параметры подключения к БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='maratzaripov',
    password=''
)


# Функция для выполнения SQL-запросов
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Функция для вставки данных в таблицу из файла CSV
def insert_data(table_name, file_name):
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            columns = ', '.join(row.keys())
            values = "', '".join(row.values())
            query = f"INSERT INTO {table_name} ({columns}) VALUES ('{values}');"
            execute_query(query)


# Вставка данных в таблицу employees
insert_data('employees', 'north_data/employees_data.csv')

# Вставка данных в таблицу customers
insert_data('customers', 'north_data/customers_data.csv')

# Вставка данных в таблицу orders
insert_data('orders', 'north_data/orders_data.csv')

print("Данные успешно загружены в таблицы.")
