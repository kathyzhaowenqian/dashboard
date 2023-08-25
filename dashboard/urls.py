from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('salesdata',views.SalesData.as_view()),
    path('salesdatadetail',views.SalesDataDetail.as_view()),
    path('test404',views.Test404.as_view()),
    path('barrace',views.Barrace.as_view())
]
