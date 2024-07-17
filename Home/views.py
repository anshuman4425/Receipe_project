from django.shortcuts import render

from django.http import HttpResponse

def Honey(Request):
    return HttpResponse('hii')
    

def hello(Request):
    people = [
        {'name' : 'anshuman', 'age': 36},
        {'name' : 'rahul', 'age': 39},
        {'name' : 'yuvrajman', 'age': 32},
        {'name' : 'krishnaan', 'age': 35},
    ]
    return render(Request, "index.html", context={'people' : people})