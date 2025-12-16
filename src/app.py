import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    current_user,
    logout_user,
)

from src.form import LoginForm, LogoutForm
from src.auth import auth
from src.auth import session_auth
from src.logger import logger


def create_app():
    load_dotenv()
    app = Flask(__name__)
    secret_key_value = os.getenv("SECRET_KEY")
    if not secret_key_value:
        raise ValueError("SECRET_KEY environment variable not set")
    app.secret_key = secret_key_value
    login_manager = LoginManager()
    login_manager.init_app(app)
    logger.info("Application initialized")

    @login_manager.user_loader
    def load_user(user_id):
        return session_auth(user_id)

    @app.route("/")
    def root():
        return redirect("/login")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("score_board"))

        login_form = LoginForm(request.form)
        if request.method == "POST" and login_form.validate():
            user = auth(login_form)
            if user:
                login_user(user)
                if user.is_admin:
                    logger.info(f"Admin {user.id} logged in.")
                    flash("Logged in as admin.")
                    return redirect(url_for("admin"))
                else:
                    logger.info(f"User {user.id} logged in.")
                    flash("Logged in successfully.")
                    return redirect(url_for("score_board"))
            else:
                logger.warning(
                    f"Failed login attempt for username: {login_form.username.data}"
                )
                flash("Invalid username or password")

        return render_template("login.html", form=LoginForm())

    @app.post("/logout")
    @login_required
    def logout():
        logout_user()
        session.clear()
        flash("Logged out successfully.")
        return redirect(url_for("login"))

    @app.route("/score-board")
    @login_required
    def score_board():
        logout_form = LogoutForm()
        return render_template("score.html", form=logout_form)

    @app.route("/admin")
    @login_required
    def admin():
        if not current_user.is_admin:
            flash("Access denied.")
            return redirect(url_for("score_board"))
        return render_template("admin.html", flag=os.getenv("FLAG"))

    return app
