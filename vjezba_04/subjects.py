#!C:\Users\Josip\AppData\Local\Programs\Python\Python38-32\python.exe
subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    };
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    };

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
};

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
};

def get_subjects():
    return subjects
    
def get_status_names():
    return status_names

def display_subject_name(subject_id, subject):
    print(subject.get('name', 'n/a') + '&nbsp;')

def display_subject_radio(subject_id, data):
    print('<input type="radio" name="' + subject_id + '" value="not" ' + ('checked>' if data.get(subject_id, 'n/a') == "not" else '>') + status_names.get('not'))
    print('<input type="radio" name="' + subject_id + '" value="enr" ' + ('checked>' if data.get(subject_id, 'n/a') == "enr" else '>') + status_names.get('enr'))
    print('<input type="radio" name="' + subject_id + '" value="pass" ' + ('checked>' if data.get(subject_id, 'n/a') == "pass" else '>') + status_names.get('pass'))

def display_subjects_by_year(year, data):
    print('<table><tr><td>' + str(year) + '. year</td><td>Ects</td><td>Status</td></tr>')
    for subject_id, subject in subjects.items():
        if(subject.get('year', 'n/a') == year):
            print('<tr><td>')
            print(subject.get('name', 'n/a'))
            print('</td><td>')
            print(str(subject.get('ects', 'n/a')))
            print('</td><td>')
            display_subject_radio(subject_id, data)
            print('</td></tr>')
    print('</table>')
    
def display_enrollment_form(data):
    total_ects = 0
    print('<table><tr><td>Enrollment form</td><td>Ects</td><td>Status</td></tr>')
    for subject_id, subject in subjects.items():
        if data.get(subject_id, 'n/a') == "enr":
            total_ects += subject.get('ects', 'n/a')
        print('<tr><td>')
        print(subject.get('name', 'n/a'))
        print('</td><td>')
        print(str(subject.get('ects', 'n/a')))
        print('</td><td>')
        print(status_names.get(data.get(subject_id, 'n/a')))
        print('</td></tr>')
    print('<tr><td>Total ects:</td><td>')
    print(str(total_ects))
    print('</td><td></td></tr></table>')
