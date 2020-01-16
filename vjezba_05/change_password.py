#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
import os
import authentication
import base
import db
from http import cookies
import session

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
session_id = get_all_cookies_object.get("session_id").value
params = cgi.FieldStorage()
session = db.get_session(session_id)
user_id = session[1].get("user_id")
user = db.get_user_by_id(user_id)
username = user[4]

if os.environ["REQUEST_METHOD"].upper() == "POST":
    password = params.getvalue("password")
    repeat_password = params.getvalue("repeat_password")
    new_password = params.getvalue("new_password")
    if password == repeat_password:
        success = authentication.change_password(username, password, new_password)
        if success:
            print('Location: login.py')
            
print()
base.start_html()

print ('''
<form method="POST">
    <h2>Change password </h2>
    
    password: 
    <input type="password" name="password"/>
    </br>

    repeat password: 
    <input type="password" name="repeat_password"/>
    </br>

    new password: 
    <input type="password" name="new_password"/>
    </br>
    
    <input type="submit" value="Change"/>
</form>
''')

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Error</div>")
base.finish_html()