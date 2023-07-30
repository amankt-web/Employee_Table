from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    if request.method=="POST":
        check = request.POST['check']
        print(check)
        
    date_time = datetime.datetime.now()
    isActive= True
    name ="Learnthecode"
    list_of_programs=[
        "wap to check the prime number",
        "wap to check odd or even from the input",
        "wap to print all prime numbers from 1 to 100"
    ]

    student = {
        'student_name':"Aman",
        'student_college': "ABS",
        'student_city':"Pune"
    }

    data ={
        'date':date_time,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):
    print("test function called from views")
    return render(request,"about.html")

def services(request):
    print("test function called from views")
    return render(request,"services.html")
