from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='loginpage')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First Name":
                fn=value
            if key=="Last Name":
                ln=value
            if key=="Sex":
                s=value
            if key=="Email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')