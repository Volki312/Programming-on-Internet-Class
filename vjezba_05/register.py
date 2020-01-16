#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
import os
import authentication
import base

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    email = params.getvalue("email")
    password = params.getvalue("password")
    repeat_password = params.getvalue("repeat_password")
    if password == repeat_password :
        success = authentication.register(email, username, password)
        if success:
            print('Location: login.py')
            
print()
base.start_html()
print ('''
<form method="POST">
    <h2>Register </h2>

    email: 
    <input type="email" name="email" />
    </br>
    
    username: 
    <input type="text" name="username" />
    </br>
    
    password: 
    <input type="password" name="password"/>
    </br>

    repeat password: 
    <input type="password" name="repeat_password"/>
    </br>
    
    <input type="submit" value="Register"/>
</form>
''')
print('<a class="btn" href="login.py">Login</a>')

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error</div>")
base.finish_html()