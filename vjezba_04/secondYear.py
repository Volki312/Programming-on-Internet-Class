#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import base
import subjects
import os
import cgi
import session

params = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)
	
data = session.get_session_data()


print()
base.start_html()
base.print_navigation()

print('<form action="thirdYear.py" method="POST">')
subjects.display_subjects_by_year(2, data)
print('<input type="submit" value="Submit"></form>')

base.finish_html()