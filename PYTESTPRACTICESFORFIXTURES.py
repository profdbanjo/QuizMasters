# This is a sample Python script.
import self as self
from flask import Flask, request, redirect, url_for


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def cause_a_to_do_something():
    import a
    a.do_something()

import sys
import pytest
xfail = pytest.mark.xfail
@pytest.mark.xfail
def test_login_failing():
    assert sgudksj@username

def test_signup_failing():
    assert sgudksj@username

def test_signup_passing():
    if userinput == username:
        userinput = input("Password?\n")
    if userinput == password:
       print("Welcome!")
    else:
       print("That is the wrong password.")
    print("That is the wrong username.")



pass_stmt =  "pass"
@pytest.mark.parametrize(
    "user, pass",
    [("valid_user@gmail.com", "12345678"), ("invalid_user@gmail.com", "00000000")],)


class Config:
    SECRET_KEY = 'Some very long secret key'




class UserMixin:
    pass


UserMixin
class User(UserMixin):
    pass


class LoginManager:
    pass


login_manager = LoginManager()


@login_manager.user_loader
def user_loader(email):
    print('[[')
    if email != 'test@gmail.com':
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email != 'test@gmail.com':
        return

    user = User()
    user.id = email

    user.is_authenticated = request.form['password'] == 'test'

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    raise Unauthorized()


def logout_user():
    pass


def login_required(args):
    pass


def login_user(user):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        return 'Ok'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method != 'POST':
            raise MethodNotAllowed()

        if request.form['email'] == 'test@gmail.com' and request.form['password'] == 'test':
            user = User()
            user.id = request.form['email']
            login_user(user)
            return redirect(url_for('.index'))

        raise Unauthorized()

    @app.route('/logout')
    def logout():
        logout_user()
        return 'Logged out'

    return app
