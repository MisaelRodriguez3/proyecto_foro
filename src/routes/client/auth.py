from flask import Blueprint, render_template

auth = Blueprint("auth_client", __name__)

@auth.route("/login")
def login_page():
    return render_template("login.html")

@auth.route("/register")
def register_page():
    return render_template("register.html")