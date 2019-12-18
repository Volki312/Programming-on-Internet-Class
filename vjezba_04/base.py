#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe

def start_html():
    print ("""<!DOCTYPE html>
    <html>
    <body>""")

def finish_html():
    print ("""</body>
    </html>""")

def print_navigation():
    print ('''
    <div>
    <a href="firstYear.py">1. year</a>
    <a href="secondYear.py">2. year</a>
    <a href="thirdYear.py">3. year</a>
    <a href="enrollmentForm.py">Enrollment Form</a>	
    </div>
    ''')