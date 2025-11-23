from django.urls import path
from . import views

urlpatterns = [
    # صفحه اصلی سایت
    path('', views.home, name='home'),
]
