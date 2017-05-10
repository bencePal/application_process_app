import ui
import config


def firstname_lastname_mentors():
    cursor = config.connection().cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    return ui.print_query_table(cursor, "")


def nickname_miskolc_mentors():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT nick_name FROM mentors
        WHERE city = 'Miskolc'
        ;""")
    return ui.print_query_table(cursor, "")


def carol_and_her_hat():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
        WHERE first_name = 'Carol'
        ;""")
    return ui.print_query_table(cursor, "")


def another_girl_hat():
    cursor = config.connection().cursor()
    cursor.execute("""
        SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
        WHERE email LIKE '%@adipiscingenimmi.edu'
        ;""")
    return ui.print_query_table(cursor, "")


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
    return ui.print_query_table(cursor, "")


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
    return ui.print_query_table(cursor, "")


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
    return ui.print_query_table(cursor, "All the mentors")


def all_data_applicants():
    # create a psycopg2 cursor that can execute queries
    cursor = config.connection().cursor()
    # run the query
    cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
    # return in table format
    return ui.print_query_table(cursor, "All the applicants")
