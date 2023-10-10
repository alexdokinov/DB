import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Teachers (
    teacher_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
''')

cursor.execute('''
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    name_of_course TEXT,
    teacher_id INTEGER,
    type_of_course INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
''')

cursor.execute('''
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birthdate DATE,
    city TEXT
);
''')

cursor.execute('''
CREATE TABLE Results (
    result_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    type_of_course INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (type_of_course) REFERENCES Courses(type_of_course)
);
''')
