from src.user_data import ADMIN, USERS


def auth(login_form):
    for user in USERS + [ADMIN]:
        if (
            user.id == login_form.username.data
            and user.password == login_form.password.data
        ):
            return user
    return None


def session_auth(user_id):
    for user in USERS + [ADMIN]:
        if user.id == user_id:
            return user
    return None
