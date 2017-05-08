import ui
import config


def firstname_lastname_mentors():
    cursor = config.connection().cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def nickname_miskolc_mentors():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT nick_name FROM mentors
        WHERE city = 'Miskolc'
        ;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def carol_and_her_hat():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
        WHERE first_name = 'Carol'
        ;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def another_girl_hat():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
        WHERE email LIKE '%@adipiscingenimmi.edu'
        ;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def add_new_applicant():
    cursor = config.connection().cursor()
    cursor.execute("""
        INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
        VALUES (11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
        ;""")
    cursor.execute("""
        SELECT * FROM applicants
        WHERE application_code = 54823
        ;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def change_phonenumber():
    cursor = config.connection().cursor()
    cursor.execute("""
        UPDATE applicants
        SET phone_number = '003670/223-7459'
        WHERE first_name = 'Jemima' AND last_name = 'Foreman'
        ;""")
    cursor.execute("""
        SELECT phone_number FROM applicants
        WHERE first_name = 'Jemima' AND last_name = 'Foreman'
        ;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "")


def del_arsiano_and_his_friend():
    cursor = config.connection().cursor()
    cursor.execute("""
        DELETE FROM applicants
        WHERE email LIKE '%@mauriseu.net'
        ;""")
    all_data_applicants()


def all_data_mentors():
    cursor = config.connection().cursor()
    cursor.execute("""SELECT * FROM mentors ORDER BY id;""")
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return ui.print_table(rows, "All the mentors")


def all_data_applicants():
    # create a psycopg2 cursor that can execute queries
    cursor = config.connection().cursor()
    # run the query
    cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
    # Fetch the result of the last execution
    rows = list(cursor.fetchall())
    # insert column header
    rows.insert(0, [row[0] for row in cursor.description])
    # return in table format
    return ui.print_table(rows, "All the applicants")
