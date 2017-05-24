import queries
import common


def choose():
    inputs = common.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        queries.firstname_lastname_mentors(common.get_cursor())
    elif option == "2":
        queries.nickname_miskolc_mentors(common.get_cursor())
    elif option == "3":
        queries.carol_and_her_hat(common.get_cursor())
    elif option == "4":
        queries.another_girl_hat(common.get_cursor())
    elif option == "5":
        queries.add_new_applicant(common.get_cursor())
    elif option == "6":
        queries.change_phonenumber(common.get_cursor())
    elif option == "7":
        queries.del_arsiano_and_his_friend(common.get_cursor())
    elif option == "8":
        queries.all_data_mentors(common.get_cursor())
    elif option == "9":
        queries.all_data_applicants(common.get_cursor())
    elif option == "0":
        exit()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["firstnames and lastnames from mentors",
               "nick_name-s of all mentors working at Miskolc",
               "Carol and her hat",
               "who is the another girl?",
               "add the new applicant",
               "change the phonenumber for Jemima Foreman",
               "delete Arsiano and his friend",
               "all data from mentors table",
               "all data from applicants table"]

    common.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        try:
            handle_menu()
            choose()
        except Exception as err:
                common.print_error_message(err)


if __name__ == '__main__':
    main()
