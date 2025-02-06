from django.urls import path
from job_application import views


urlpatterns = [
    path('',views.index,name='index'),

]