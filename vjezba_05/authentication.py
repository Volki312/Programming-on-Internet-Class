#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import db
import password_utils


def register(email, username, password):
    user_id = db.create_user(email, username, password.encode('utf-8'))
    # user_id = db.create_user(username, password)
    if user_id:
        return True
    else:
        return False


def authenticate(username, password):
    user = db.get_user_by_username(username)
    if user and password_utils.verify_password(password.encode('utf-8'), user[2].encode('utf-8')):
        # if (user and password_utils.verify_password(password, user[2])):
        return True, user[0]
    else:
        return False, None

def change_password(username, old_password, new_password):
    user = db.get_user_by_username(username)
    if user and password_utils.verify_password(old_password.encode('utf-8'), user[2].encode('utf-8')):
        success = db.change_user_password(username, new_password.encode('utf-8'))
        if success:
            return True
        else:
            return False
