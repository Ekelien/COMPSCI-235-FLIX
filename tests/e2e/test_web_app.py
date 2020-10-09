from os import environ

import pytest
from dotenv import load_dotenv
from flask import session

from TEST_DATA_PATH import PATH

load_dotenv()


def write():
    user_file = open(PATH + "\\user.csv", "w")
    user_file.write("""id,username,password,favorite
0,ekelien,pbkdf2:sha256:150000$JgNuBVC5$4566450fcfe0db298d94730bd7303391187f2638148cda6c47006b93aed4e637,"1,0"
1,super,pbkdf2:sha256:150000$Z9hVJaXY$8c110ffb94a661338ee54c50460c5bea2459e7cfd76baf763c541405a78d9bfa,""")


def test_dotenv_config():
    assert environ.get('FLASK_APP') == 'wsgi.py'


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Editor's Pick" in response.data


def test_first_click_user(client):
    response = client.get('/user/check')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/user/login'


def test_register(client):
    response_code = client.get('/user/register').status_code
    assert response_code == 200
    response = client.post(
        '/user/register',
        data={'username': 'hongmi', 'password': 'super0000'}
    )
    assert response.headers['Location'] == 'http://localhost/user/login'
    write()


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('cj', '', b'Your username is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test', b"Your password must contain at least 8 characters, with at least one letter and one digit."),
        ('super', 'Test#6^0', b'Your username is already taken - please supply another'),
))
def test_register_with_invalid_input(client, username, password, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/user/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/user/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['username'] == 'super'


#
#
def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_login_required_to_comment(client):
    response = client.post('/comment?id=0')
    assert response.headers['Location'] == 'http://localhost/user/login'
