#!C:\Users\Stana\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
password = form.getvalue("password")
passwordRepeat = form.getvalue("passwordRepeat")

if password != passwordRepeat:
    print('Refresh: 1; URL=login.py')

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Info</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    
        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="../../assets/js/html5shiv.js"></script>
        <script src="../../assets/js/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <form class="form-horizontal" action="additionalInfo.py" method="post">
            <fieldset>
                <!-- Info form -->
                <legend>Info</legend>
                
                <!-- Status -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="status">Status:</label>
                    <label class="radio-inline" for="status-0"><input type="radio" name="status" id="status-0" value="Full-time" checked="checked">Full-time</label> 
                    <label class="radio-inline" for="status-1"><input type="radio" name="status" id="status-1" value="Part-time">Part-time</label>
                </div>
                
                <!-- Email-->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="email">E-mail:</label>  
                    <input id="email" name="email" type="email" placeholder="josip312@hotmail.com" class="form-control input-md" required="">
                </div>
                
                <!-- Course -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="course">Course:</label>
                    <select id="course" name="course" class="form-control">
                        <option value="IT">IT</option>
                        <option value="BP">BP</option>
                        <option value="RM">RM</option>
                        <option value="IS">IS</option>
                    </select>
                </div>
                
                <!-- Final exam -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="hasFinal">Final exam:</label>
                    <label class="checkbox-inline" for="hasFinal-0"><input type="checkbox" name="hasFinal" id="hasFinal-0" value="Yes"></label>
                </div>
                
                <!-- Parameters -->
                <input type="hidden" name="name" value="{name}">
                
                <!-- Submit -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <button id="submit" name="submit" class="btn btn-primary">Next</button>
                </div>
            </fieldset>
        </form>
    </body>
</html>
'''.format(name=name))
