from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("pasword1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(firstName) < 2:
            flash("FirstName must be greater than 1 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        elif len(password1) < 7:
            flash("Passwords must be atleast 7 characters.", category="error")
        else:
            flash("Account created!", category="success")

        #add user to the database



    return render_template("sign_up.html", user=current_user)
