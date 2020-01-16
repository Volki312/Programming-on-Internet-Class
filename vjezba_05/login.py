#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import base
import os, cgi
import session
import authentication

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = authentication.authenticate(username, password)
    if success:
        session_id = session.create_session()
        session.add_to_session({"user_id": user_id}, session_id=session_id)
        print('Location: upload.py')

print("Content-type:text/html")
print("")
base.start_html()

print('''
<form method="POST">
    <h2>Login </h2>

    username: 
    <input type="text" name="username" />
    </br>
    
    password: 
    <input type="password" name="password"/>
    </br>
    
    <input type="submit" value="Login"/>
</form>
''')
print('<a class="btn" href="register.py">Register</a>')

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Login Error</div>")
base.finish_html()
