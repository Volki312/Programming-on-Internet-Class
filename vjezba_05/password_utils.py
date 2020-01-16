#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import bcrypt

salt = bcrypt.gensalt()


def hash_password(password):
    hashed = bcrypt.hashpw(password, salt)
    # hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password(password, hash):
    # password = password.encode('utf-8')
    # hash = hash.encode('utf-8')
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False
