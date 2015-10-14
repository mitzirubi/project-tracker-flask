from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github)
    return html


@app.route("/add_student_form")
def get_add_student():
    
    return render_template("student_add.html")


@app.route("/add_student")
def add_student():
    
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    github = request.args.get('github')

    first_name, last_name, github = hackbright.make_new_student(first_name,last_name,github)
    html = render_template('student_add_confirm.html',
                            first=first_name,
                            last=last_name,
                            github=github)
    return html




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
