import mysql.connector

# Step 1: Connect to MySQL
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Change this to your MySQL server's host
        user="your_username",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="your_database"  # Replace with your database name
    )
    return connection

# Step 2: Create Tables
def create_tables(connection):
    cursor = connection.cursor()

    # Creating the STUDENT table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT (
            STUDENT_ID INT PRIMARY KEY,
            STUDENT_NAME VARCHAR(100),
            AGE INT,
            HOBBY VARCHAR(100),
            DOB DATE,
            DOOR_NO VARCHAR(10),
            STREET VARCHAR(100),
            CITY VARCHAR(100),
            STATE VARCHAR(100),
            PIN VARCHAR(10)
        );
    """)

    # Creating the LECTURER table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LECTURER (
            LECTURER_ID INT PRIMARY KEY,
            LECTURER_NAME VARCHAR(100)
        );
    """)

    # Creating the COURSE table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COURSE (
            COURSE_ID INT PRIMARY KEY,
            COURSE_NAME VARCHAR(100)
        );
    """)

    # Creating the SUBJECTS table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SUBJECTS (
            SUBJECT_ID INT PRIMARY KEY,
            SUBJECT_NAME VARCHAR(100)
        );
    """)

    # Creating the STUDENT_COURSE table (junction table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT_COURSE (
            STUDENT_ID INT,
            COURSE_ID INT,
            PRIMARY KEY (STUDENT_ID, COURSE_ID),
            FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(STUDENT_ID),
            FOREIGN KEY (COURSE_ID) REFERENCES COURSE(COURSE_ID)
        );
    """)

    # Creating the LECTURER_COURSE table (junction table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LECTURER_COURSE (
            LECTURER_ID INT,
            COURSE_ID INT,
            PRIMARY KEY (LECTURER_ID, COURSE_ID),
            FOREIGN KEY (LECTURER_ID) REFERENCES LECTURER(LECTURER_ID),
            FOREIGN KEY (COURSE_ID) REFERENCES COURSE(COURSE_ID)
        );
    """)

    # Creating the COURSE_SUBJECT table (junction table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COURSE_SUBJECT (
            COURSE_ID INT,
            SUBJECT_ID INT,
            PRIMARY KEY (COURSE_ID, SUBJECT_ID),
            FOREIGN KEY (COURSE_ID) REFERENCES COURSE(COURSE_ID),
            FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(SUBJECT_ID)
        );
    """)

    connection.commit()
    print("Tables created successfully.")

# Step 3: Insert Data into Tables
def insert_data(connection):
    cursor = connection.cursor()

    # Inserting into STUDENT table
    cursor.executemany("""
        INSERT INTO STUDENT (STUDENT_ID, STUDENT_NAME, AGE, HOBBY, DOB, DOOR_NO, STREET, CITY, STATE, PIN)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, [
        (1, 'John Doe', 20, 'Reading', '2003-05-15', '12A', 'Maple Street', 'New York', 'NY', '10001'),
        (2, 'Jane Smith', 22, 'Cycling', '2001-03-22', '25B', 'Pine Avenue', 'San Francisco', 'CA', '94102')
    ])

    # Inserting into LECTURER table
    cursor.executemany("""
        INSERT INTO LECTURER (LECTURER_ID, LECTURER_NAME)
        VALUES (%s, %s);
    """, [
        (1, 'Dr. Emily Brown'),
        (2, 'Dr. Robert Wilson')
    ])

    # Inserting into COURSE table
    cursor.executemany("""
        INSERT INTO COURSE (COURSE_ID, COURSE_NAME)
        VALUES (%s, %s);
    """, [
        (101, 'Computer Science 101'),
        (102, 'Mathematics 101')
    ])

    # Inserting into SUBJECTS table
    cursor.executemany("""
        INSERT INTO SUBJECTS (SUBJECT_ID, SUBJECT_NAME)
        VALUES (%s, %s);
    """, [
        (1, 'Data Structures'),
        (2, 'Algorithms'),
        (3, 'Calculus'),
        (4, 'Linear Algebra')
    ])

    # Inserting into STUDENT_COURSE table (junction)
    cursor.executemany("""
        INSERT INTO STUDENT_COURSE (STUDENT_ID, COURSE_ID)
        VALUES (%s, %s);
    """, [
        (1, 101),  # John Doe attends Computer Science 101
        (2, 102)   # Jane Smith attends Mathematics 101
    ])

    # Inserting into LECTURER_COURSE table (junction)
    cursor.executemany("""
        INSERT INTO LECTURER_COURSE (LECTURER_ID, COURSE_ID)
        VALUES (%s, %s);
    """, [
        (1, 101),  # Dr. Emily Brown teaches Computer Science 101
        (2, 102)   # Dr. Robert Wilson teaches Mathematics 101
    ])

    # Inserting into COURSE_SUBJECT table (junction)
    cursor.executemany("""
        INSERT INTO COURSE_SUBJECT (COURSE_ID, SUBJECT_ID)
        VALUES (%s, %s);
    """, [
        (101, 1),  # Computer Science 101 has the subject Data Structures
        (101, 2),  # Computer Science 101 has the subject Algorithms
        (102, 3),  # Mathematics 101 has the subject Calculus
        (102, 4)   # Mathematics 101 has the subject Linear Algebra
    ])

    connection.commit()
    print("Data inserted successfully.")

# Step 4: Main Execution
def main():
    connection = create_connection()
    create_tables(connection)
    insert_data(connection)
    connection.close()

if __name__ == "__main__":
    main()
