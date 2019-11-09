#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
status = form.getvalue("status")
email = form.getvalue("email")
course = form.getvalue("course")
hasFinal = form.getvalue("hasFinal")
remark = form.getvalue("remark")

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Final Page</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">

        <style>
            table, th, td {{ 
                border: 1px solid black;
            }}
        </style>

        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="../../assets/js/html5shiv.js"></script>
        <script src="../../assets/js/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <table>
            <tr><th colspan="2">Final data</th></tr>
            <tr>
                <td>Name:</td>
                <td>{name}</td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td>{email}</td>
            </tr>
            <tr>
                <td>Status:</td>
                <td>{status}</td>
            </tr>
            <tr>
                <td>Course:</td>
                <td>{course}</td>
            </tr>
            <tr>
                <td>Has final:</td>
                <td>{hasFinal}</td>
            </tr>
            <tr>
                <td>Remark:</td>
                <td>{remark}</td>
            </tr>
        </table>
        <a href="login.py">Back to homepage</button>
    </body>
</html>
'''.format(name=name, email=email, status=status, course=course, hasFinal=hasFinal, remark=remark))
