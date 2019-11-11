#!C:\Users\Stana\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
status = form.getvalue("status")
email = form.getvalue("email")
course = form.getvalue("course")
if form.getvalue("hasFinal"):
    hasFinal = form.getValue("hasFinal")
else:
    hasFinal = "Has no final"

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Additional Info</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">

        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="../../assets/js/html5shiv.js"></script>
        <script src="../../assets/js/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <form class="form-horizontal" action="post.py" method="post">
            <fieldset>
                <!-- Additional Info form -->
                <legend>Additional Info</legend>

                <!-- Remark -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="remark">Remark:</label>
                    <div class="col-md-4">                     
                        <textarea class="form-control" id="remark" name="remark" placeholder="Leave your remark here..." rows="10" cols="30"></textarea>
                    </div>
                </div>

                <!-- Parameters -->
                <input type="hidden" name="name" value="{name}">
                <input type="hidden" name="status" value="{status}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="course" value="{course}">
                <input type="hidden" name="hasFinal" value="{hasFinal}">
                
                <!-- Submit -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <div class="col-md-4">
                        <button id="submit" name="submit" class="btn btn-primary">Finish</button>
                    </div>
                </div>
            </fieldset>
        </form>
    </body>
</html>
'''.format(name=name, email=email, status=status, course=course, hasFinal=hasFinal))
