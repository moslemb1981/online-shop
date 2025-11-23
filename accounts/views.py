from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("صفحه ورود - فعلاً تست")

def logout_view(request):
    return HttpResponse("صفحه خروج - فعلاً تست")

def profile_view(request):
    return HttpResponse("پروفایل کاربر - تست")
