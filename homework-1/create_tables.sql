-- SQL-команды для создания таблиц
create table employees (
	employee_id serial primary key,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes text
);


create table customers (
	customer_id varchar primary key,
	company_name varchar(100),
	contact_name varchar(100)
);


create table orders (
	order_id serial primary key,
	customer_id varchar references customers(customer_id),
	employee_id int references employees(employee_id),
	order_date date,
	ship_city varchar(100)
);

