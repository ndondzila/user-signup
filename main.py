from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('inputs.html')

@app.route("/", methods=["POST"])
def validation():

    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    empty_fields_error = ''

    if len(username) == 0 or len(password) == 0 or len(verify_password) == 0:
        empty_fields_error = 'Please make sure to fill out all required fields'

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'Please enter a username that is between 3 and 20 characters long.'
    if len(password) < 3 or len(password) > 20:
        password_error = 'Please enter a password that is between 3 and 20 characters long.'
    if password != verify_password:
        verify_error = 'Your passwords did not match, please re-enter matching passwords.'
    if len(email) > 0:
        email_error = 'Please enter a valid email address.'
        if len(email) < 20 and len(email) > 3:
            for i in email:
                if i == '@':
                    for l in email:
                        if l == '.':
                            email_error = ''
                            for j in email:
                                if j ==' ':
                                    email_error = 'Please enter a valid email address with an "@" and a "." and no spaces, between 3 and 20 characters long.'

    if username_error == password_error == verify_error == email_error == empty_fields_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('inputs.html', username=username, email=email, empty_fields_error=empty_fields_error, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()