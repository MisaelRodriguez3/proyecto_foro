from flask import Blueprint, render_template
from flask_login import current_user, login_required
from src.service import getAllPostByUser


user = Blueprint("user", __name__)

@user.route("/profile")
@login_required
def profile():
    return render_template("profile.html", logged = current_user.is_authenticated, user = current_user, posts=getAllPostByUser(current_user.usuario_Id))
