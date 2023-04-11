from django.shortcuts import render
import mysql.connector as sql
fn = ''
ln = ''
g = ''
dob = ''
em = ''
pwd = ''
cpwd = ''
mb = ''
# Creating views here.


def signaction(request):
    global fn, ln, g, dob, em, pwd, cpwd, mb
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="Mahesh@021011", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "gender":
                g = value
            if key == "dob":
                dob = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "confirm_password":
                cpwd = value
            if key == "mobile_number":
                mb = value

        # if pwd != cpwd:
        #     return

        c = "insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            fn, ln, g, dob, em, pwd, cpwd, mb)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')
