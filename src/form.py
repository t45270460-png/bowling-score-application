from wtforms import StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(label="ユーザ名", validators=[validators.DataRequired()])
    password = PasswordField(
        label="パスワード",
        validators=[validators.DataRequired()],
    )
    submit = SubmitField("ログイン")


class LogoutForm(FlaskForm):
    submit = SubmitField("ログアウト")
