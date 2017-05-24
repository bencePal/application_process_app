from terminaltables import SingleTable
import config


def print_query_table(cursor, title):
    # Fetch the result of the last execution
    rows = list(cursor.fetchall())
    # insert column header
    rows.insert(0, [row[0] for row in cursor.description])
    # table config
    table = SingleTable(rows)
    table.inner_row_border = True
    table.title = title
    print(table.table)


def print_menu(title, list_options, exit_message):
    print("{}".format(title))
    for index, option in enumerate(list_options, 1):
        print("({}) {}".format(index, option))
    print("(0) {}".format(exit_message))


def print_error_message(message):
    print("Error: {}\n".format(message))


def get_inputs(list_labels, title):
    inputs = []
    print("{}".format(title))
    for label in list_labels:
        inputs.append(input("{}".format(label)))
    print()

    return inputs
