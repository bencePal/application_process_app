from flask import Flask, render_template
import queries
import common

app = Flask(__name__)


@app.route("/")
def home_page():
    title = "Home page"
    return render_template("front_page.html", title=title)


@app.route("/mentors")
def mentors_and_schools_page():
    title = "Mentors and schools page"
    query = common.fetch_data(queries.mentors_and_schools(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


@app.route("/all-school")
def all_school_page():
    title = "All school page"
    query = common.fetch_data(queries.all_school(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


@app.route("/mentors-by-country")
def mentors_by_country_page():
    title = "Mentors by country page"
    query = common.fetch_data(queries.mentors_by_country(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


@app.route("/contacts")
def contacts_page():
    title = "Contacts page"
    query = common.fetch_data(queries.contacts(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


@app.route("/applicants")
def applicants_page():
    title = "Applicants page"
    query = common.fetch_data(queries.applicants(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


@app.route("/applicants-and-mentors")
def applicants_and_mentors_page():
    title = "Applicants and mentors page"
    query = common.fetch_data(queries.applicants_and_mentors_(common.get_cursor()))
    return render_template("page.html", title=title, table=query)


if __name__ == '__main__':
    app.run(debug=True)
