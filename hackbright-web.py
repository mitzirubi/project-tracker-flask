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


@app.route("/add_student", methods=["POST"]) #this can be a list and its methods can take multiple methods
def add_student():
    # if request.method == "GET": (this is WAY#1 of having 2 forms end in the same route)

    first_name = request.form['first_name']     #.get('first_name')]
    last_name = request.form['last_name']                        #.get('last_name')
    github = request.form['github']                    #get('github')

    #success = hackbright.make_new_student(first_name,last_name,github) (another way of testing)
    hackbright.make_new_student(first_name,last_name,github)

     #whether or not we return something
    # first_name, last_name, github = hackbright.make_new_student(first_name,last_name,github)
    html = render_template('student_add_confirm.html',
                            first_name=first_name,
                            last_name=last_name,
                            github=github)
    return html


# @app.route("/joel", methods=["GET"]) WAY#2:we can create same app route with 2 functions. 
#     ...

# @app.route("/joel", methods=["POST"])
# def joel_post():
#     ...



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
