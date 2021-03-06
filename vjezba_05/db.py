#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import mysql.connector

import json
import password_utils
import os
from datetime import datetime

db_conf = {
    "host": "localhost",
    "db_name": "vj_5",
    "user": "root",
    "passwd": ""
}


def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb


# CRUD sessions

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid


def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])


def replace_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
                   (session_id, json.dumps(data)))
    mydb.commit()


def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


# CRUD users

def create_user(email, username, password):
    query = "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password, email, 'user')
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        if not get_user_by_username(username) and not get_user_by_email(email):
            cursor.execute(query, values)
            mydb.commit()
    except:
        return None
    return cursor.lastrowid


def get_user_by_username(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = cursor.fetchone()
    return myresult


def get_user_by_email(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE email='" + email + "'")
    myresult = cursor.fetchone()
    return myresult
    

def get_user_by_id(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult


def get_users():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    return myresult


def change_user_password(username, new_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    hashed_password = password_utils.hash_password(new_password)
    query = "UPDATE users SET password=%s WHERE username=%s"
    values = (hashed_password, username)
    try:
        cursor.execute(query, values)
        mydb.commit()
        return True
    except:
        
        return False
#    mydb = get_DB_connection()
#    cursor = mydb.cursor()
#    # user = get_user_by_username(username)
#    hashed_password = password_utils.hash_password(new_password)
#    try:
#        cursor.execute("UPDATE users SET 'password'=%s WHERE username=%s" % (hashed_password, username))
#        mydb.commit()
#        return True
#    except:
#        return False


def delete_user(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM users WHERE user_id='" + str(user_id) + "'")
    mydb.commit()


# CRUD images

def save_image(file, collection_name):
    mydb = get_DB_connection()
    collection_id = get_collection_id_by_name(collection_name)[0]
    cursor = mydb.cursor()
    cursor.execute(
        "INSERT into images (path, counter, created, last, collection_id) VALUES('%s', % d, '%s', '%s', '%s')" % (
            collection_name + "/" + file.filename, 0, str(datetime.now()), str(datetime.now()), collection_id))
    mydb.commit()
    return cursor.lastrowid


def get_image_by_id(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM images where image_id=%s" % id)
    return cursor.fetchone()


def get_image_by_path(path):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM images where path='%s'" % path)
    return cursor.fetchone()


def get_images_by_collection_id(collection_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * from images where collection_id = %s" % str(collection_id))
    images = cursor.fetchall()
    return images


def get_all_images():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM images")
    images = cursor.fetchall()
    return images


def visit_image(image_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("Update images set counter = counter + 1, last = '%s' where image_id=%d" % (str(datetime.now()), image_id))
    mydb.commit()


def delete_image(img_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    # img = get_image_by_id(img_id)
    try:
        cursor.execute("DELETE FROM images where image_id = %s" % str(img_id))
        mydb.commit()
        return True
    except:
        return False


# CRUD collections

def save_collection(collection_name):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    collection_id = get_collection_id_by_name(collection_name)

    if not collection_id:
        try:
            cursor.execute("INSERT INTO collections (name) VALUES ('%s')" % collection_name)
            mydb.commit()
        except:
            print("INSERT INTO collections (name) VALUES ('%s')" % collection_name)
            return None
        os.mkdir('../../htdocs/images/' + str(collection_name))
        return cursor.lastrowid
    else:
        return collection_id[0]


def get_collection_id_by_name(collection_name):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("Select * from collections where name = '%s'" % collection_name)
    collection_id = cursor.fetchone()
    return collection_id


def get_collections():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM collections")
    myresult = cursor.fetchall()
    return myresult
