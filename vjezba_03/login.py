#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import cgitb

cgitb.enable(display=0, logdir="")

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">

        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="../../assets/js/html5shiv.js"></script>
        <script src="../../assets/js/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <form class="form-horizontal" action="info.py" method="post">
            <fieldset>
                <!-- Login form -->
                <legend>Login</legend>

                <!-- Name -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="name">Name:</label>  
                    <div class="col-md-4">
                        <input id="name" name="name" type="text" value="" placeholder="Josip" class="form-control input-md" required="">   
                    </div>
                </div>

                <!-- Password -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="password">Password:</label>
                    <div class="col-md-4">
                        <input id="password" name="password" type="password" value="" placeholder="******" class="form-control input-md" required="">
                    </div>
                </div>

                <!-- Password repeat -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="passwordRepeat">Repeat password:</label>
                    <div class="col-md-4">
                        <input id="passwordRepeat" name="passwordRepeat" type="password" value="" placeholder="******" class="form-control input-md" required="">
                    </div>
                </div>

                <!-- Submit -->
                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <div class="col-md-4">
                        <button id="submit" name="submit" class="btn btn-primary">Next</button>
                    </div>
                </div>
            </fieldset>
        </form>
    </body>
</html>
''')