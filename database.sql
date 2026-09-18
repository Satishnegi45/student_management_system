create database student_management;

use student_management;

create table students(
	 student_id int primary key identity(1,1),
	 name varchar(100) not null,
	 age int,
	 course varchar(100),
	 marks decimal(5,2),
	 grade varchar(5)
)

select * from students;

insert into students (name, age, course, marks, grade)
values
('rahul', 20, 'computer engineering', 85.50, 'a'),
('priya', 21, 'computer engineering', 78.00, 'b'),
('amit', 20, 'information technology', 91.00, 'a+'),
('neha', 22, 'computer engineering', 67.50, 'c'),
('rohit', 21, 'information technology', 73.00, 'b');















