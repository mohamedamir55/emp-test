from django.shortcuts import render,redirect
from models import EMP

# Create your views here.def
def home(request):
    return render (request,'home.html')


def add(request):
    
    if request.method =='POST':
        if choise =='1':
            name=request.POST.get('name')
            age=request.POST.get('age')
            salary=request.POST.get('salary')
            EMP.objects.create(name=name,age=age,salary=salary)
        
    return redirect ('home.html')

def print (request):
    if request.method =='POST':
        if choise =='2':
            return f'{name} and his age {age} anad his salary is {salary}'

def delete (request,id):
    if request.method=='POST':
        if choise =='3':
            name=request.POST.get('name')
            age=request.POST.get('age')
            emp=EMP.objects.get(name=name,age=age,id=id)
            emp.delete()

def update(request,id):
    
    if request.method=='POST':
        if choise =='3':
            new_name=request.POST.get('name')
            new_age=request.POST.get('age')
            new_salary=request.POST.get('salary')
            emp=EMP.objects.get(name=new_name,age=new_age,salary=new_salary,id=id)
            emp.update()
            emp.save()

def end (request):
    if request.method =='POST':
        if choise =='5':
            return f'thank you... end the program'
