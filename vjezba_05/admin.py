#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import db
import base
import session

images = db.get_all_images()

data = session.get_session_data()
if data is None:
  print("Location: login.py")

user = db.get_user_by_id(data['user_id'])

if user[3] != "admin":
  print("Location: upload.py")


print("Content-type:text/html")
print("")
base.start_html()
for image in images:
  print('<p>%s : was viewed %d times</p>' % (image[1], image[2]))
base.finish_html()