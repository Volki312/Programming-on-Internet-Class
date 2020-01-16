#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import base
import cgi
import os
import db
import session

images = ""
request_type = os.environ.get('REQUEST_METHOD', '')
if not os.path.isdir('../../htdocs/images'):
    os.mkdir('../../htdocs/images')

    images = os.listdir('../../htdocs/images')

form = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print("Location: login.py")

print("Content-type:text/html")
print("")
base.start_html()
if request_type == "POST":
    file_item = form["avatar"]

    collection = form.getvalue('collection')
    if not collection:
        collection = form.getvalue('collection_select')
    collection_id = db.save_collection(str(collection))

    if file_item.filename:
        fn = ('../../htdocs/images/' + str(collection) + "/")
        fn += os.path.basename(file_item.filename)
        db.save_image(file_item, collection)
        open(fn, 'wb').write(file_item.file.read(250000))
        message = '<h3>The file "' + fn + '" uploaded successfully!</h3>'
    else:
        message = "<h3>No file was uploaded</h3>"

collections = db.get_collections()


collec = "None"
if request_type == "GET":
    collec = form.getvalue('collections')
    if not collec:
        collec = "None"
        
print('<form method="GET">')
print("<h3> Selected collection: </h3>")
print("<em>" + collec + "</em></br>")
print('<select name="collections">')
for collection in collections:
    print('<option>' + collection[1] + '</option>')
print('</select>')
print('<input type="submit" value="Select">')
print("</form>")


print('<div class="imgs" style="width: max-content;">')

collec_id = db.get_collection_id_by_name(collec)[0]
db_images = db.get_images_by_collection_id(collec_id)

for image in db_images:
    print('<form action="image.py" method="POST" target="_blank" style="display: inline;">')
    print('<button type="submit">')
    print('<img src="../../images/%s" width=150 height=200>' % image[1])
    print('<input type="hidden" name="image" value="%s"/>' % image[1])
    print('<input type="hidden" name="image_id" value="%s"/>' % image[0])
    print('</button>')
    print("</form>")
print("</div>")


print('</br></br>')
print('<form enctype="multipart/form-data" method="POST" style="margin-bottom: 100px;">')
print('<input type="text" name="collection" list="db_colls">')
if collections:
    print('<select name="collection_select">')
    for collection in collections:
        print('<option>' + collection[1] + '</option>')
    print('</select>')
else:
    print('<input type="text" name="collection">')

print('<input type="file"  name="avatar" accept="image/png, image/jpeg">')
print('<input type="submit" value="Upload">')
print('</form>')

print('<a class="btn" href="logout.py">Logout</a>')
print('<a class="btn" href="change_password.py">Change password</a>')

base.finish_html()
