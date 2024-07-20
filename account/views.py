from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def login_view (request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect ('home.html')

    return render(request,'login.html')
