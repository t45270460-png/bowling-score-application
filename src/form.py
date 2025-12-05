from wtforms import StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[validators.DataRequired()])
    password = PasswordField(
        label="Password",
        validators=[validators.DataRequired()],
    )
    submit = SubmitField("ログイン")


class LogoutForm(FlaskForm):
    submit = SubmitField("ログアウト")
