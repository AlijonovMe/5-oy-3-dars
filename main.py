import psycopg2

connect = psycopg2.connect(
    database="data",
    user="postgres",
    password="2007",
    host="localhost"
)

cursor = connect.cursor()

# ------------------- Table yaratish ------------------ #

cursor.execute("""
    CREATE TABLE IF NOT EXISTS school(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        address VARCHAR(200),
        phone_number CHAR(12),
        davlat_maktabi BOOL
    );

    CREATE TABLE IF NOT EXISTS teacher(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        phone_number CHAR(12),
        school_id INTEGER REFERENCES school(id)
    );

    CREATE TABLE IF NOT EXISTS student(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        date_of_birth DATE,
        gender VARCHAR(5),
        school_id INTEGER REFERENCES school(id)
    );

    CREATE TABLE IF NOT EXISTS class(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        teacher_id INTEGER REFERENCES teacher(id),
        school_id INTEGER REFERENCES school(id)
    );

    CREATE TABLE IF NOT EXISTS subject(
        id  SERIAL PRIMARY KEY,
        name VARCHAR(100),
        class_id INTEGER REFERENCES class(id),
        teacher_id INTEGER REFERENCES teacher(id)
    );

    CREATE TABLE IF NOT EXISTS enrollment(
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(id),
        class_id INTEGER REFERENCES class(id),
        enrollment_date DATE DEFAULT CURRENT_DATE
    );
    
    CREATE TABLE IF NOT EXISTS grade(
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(id),
        subject_id INTEGER REFERENCES subject(id),
        grade_value INTEGER,
        date_given DATE DEFAULT CURRENT_DATE
    );
    
    CREATE TABLE IF NOT EXISTS attendance(
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(id),
        class_id INTEGER REFERENCES class(id),
        date DATE DEFAULT CURRENT_DATE
    );
""")

# ------------------- Yaratilgan jadvallarga ma'lumot qo'shish ------------------ #

# cursor.execute("""
#     INSERT INTO school (name, address, phone_number, davlat_maktabi)
#     VALUES ('Najot Ta''lim', 'Ferghana', '998788889888', FALSE);
#
#     INSERT INTO teacher (first_name, last_name, email, phone_number, school_id)
#     VALUES ('Qobilbek', 'Madraximov', 'qobilbek@gmail.com', '998901234567', 1);
#
#     INSERT INTO student (first_name, last_name, date_of_birth, gender, school_id)
#     VALUES ('Abdulbosit', 'Alijonov', '2024-04-10', 'Male', 1);
#
#     INSERT INTO class (name, teacher_id, school_id)
#     VALUES ('fn27', 1, 1);
#
#     INSERT INTO subject (name, class_id, teacher_id)
#     VALUES ('Backend Python Django (Standard)', 1, 1);
#
#     INSERT INTO enrollment (student_id, class_id)
#     VALUES (1, 1);
#
#     INSERT INTO grade (student_id, subject_id, grade_value)
#     VALUES (1, 1, 100);
#
#     INSERT INTO attendance (student_id, class_id)
#     VALUES (1, 1);
#
# """)

# ------------------- Jadval ma'lumotlarini olish ------------------ #

# cursor.execute("""SELECT id, first_name, last_name, TO_CHAR(date_of_birth, 'dd.mm.yyyy') AS birth_date, gender FROM student;""")
# students = cursor.fetchall()
#
# for student in students:
#     print(student)

# ------------------- 2 ta jadval nomini o'zgartirish ------------------ #

# cursor.execute("""
#     ALTER TABLE school RENAME TO training_center;
#     ALTER TABLE teacher RENAME TO instructor;
# """)
#
# cursor.execute("SELECT * FROM training_center")
# print("Training center:", cursor.fetchall())
#
# cursor.execute("SELECT * FROM instructor")
# print("Instructor:", cursor.fetchall())


# ------------------- 3 ta ustun nomini o'zgartirish ------------------ #

# cursor.execute("""
#     ALTER TABLE training_center RENAME COLUMN davlat_maktabi TO state_school;
#     ALTER TABLE instructor RENAME COLUMN phone_number TO number;
#     ALTER TABLE student RENAME COLUMN date_of_birth TO birth_date;
# """)
#
# cursor.execute("SELECT * FROM training_center")
# print("Training center:", cursor.fetchall())
#
# cursor.execute("SELECT * FROM instructor")
# print("Instructor:", cursor.fetchall())
#
# cursor.execute("SELECT * FROM student")
# print("Student:", cursor.fetchall())

# ------------------- 2 ta ustun qo'shish ------------------ #

# cursor.execute("""
#     ALTER TABLE training_center ADD COLUMN email VARCHAR(100) DEFAULT 'example@gmail.com';
#     ALTER TABLE instructor ADD COLUMN hire_date DATE DEFAULT CURRENT_DATE;
# """)
#
# cursor.execute("SELECT * FROM training_center")
# print("Training center:", cursor.fetchall())
#
# cursor.execute("SELECT * FROM instructor")
# print("Instructor:", cursor.fetchall())

# ------------------- 1 ta ustunni o'chirish ------------------- #

# cursor.execute("ALTER TABLE training_center DROP COLUMN email")
# cursor.execute("SELECT * FROM training_center")
# print("Training center:", cursor.fetchall())

# ------------------- 4 ta ma'lumotni update qilish ------------- #

# cursor.execute("""
#     UPDATE student SET birth_date = '10-04-2007' WHERE id = 1;
#     UPDATE subject SET name = 'Backend Python' WHERE id = 1;
#     UPDATE training_center SET address = 'Tashkent' WHERE id = 1;
#     UPDATE grade SET grade_value = 98 WHERE id = 1;
# """)

# ----------------- 4 ta ma'lumotni o'chirish ----------- #

# cursor.execute("""
#     DELETE FROM enrollment WHERE id = 1;
# """)
#
# cursor.execute("""
#     DELETE FROM attendance WHERE id = 1;
#     DELETE FROM grade WHERE id = 1;
# """)
#
# cursor.execute("""
#     DELETE FROM student WHERE id = 1;
# """)

# ----------- Barcha jadvallarni tozalash ( kerak bo'lib qolsa ) ------------ #

# cursor.execute("""
#     DROP TABLE IF EXISTS attendance;
#     DROP TABLE IF EXISTS grade;
#     DROP TABLE IF EXISTS enrollment;
#     DROP TABLE IF EXISTS subject;
#     DROP TABLE IF EXISTS class;
#     DROP TABLE IF EXISTS student;
#     DROP TABLE IF EXISTS teacher;
#     DROP TABLE IF EXISTS school;
#     DROP TABLE IF EXISTS instructor;
#     DROP TABLE IF EXISTS training_center;
# """)


connect.commit()
cursor.close()
connect.close()
