#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
import base
import db
import os
from datetime import datetime
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

params = cgi.FieldStorage()
img = params.getvalue("image")
image = db.get_image_by_path(img)
image_id = params.getvalue("image_id")
cookies_object = cookies.SimpleCookie()
cookies_object["image_id"] = image_id
cookies_object["last_visited"] = datetime.now()
cookies_object["image_id"]['expires'] = 12 * 30 * 24 * 60 * 60
print(cookies_object.output())

last_time = get_all_cookies_object.get("last_visited")

if os.environ["REQUEST_METHOD"].upper() == "GET":
    img_id = params.getvalue("id_img")
    success = db.delete_image(img_id)
    if success:
        print("Location: upload.py")
    else:
        print(img_id)
        
if get_all_cookies_object.get("image_id"):
    db.visit_image(image[0])
    
print("Content-type:text/html")
print("")
base.start_html()
print('<img src="../../images/%s" width=600 height=400>' % image[1])
print('<form method="GET">')
print('<input type="submit" value="DELETE"/>')
print('<input type="hidden" name="id_img" value="%s"/>' % image[0])
print('</form>')
base.finish_html()
