from django.urls import path, include
from resume_app.views import *

app_name = 'resume_app'

urlpatterns = [
    path('', index_view, name= 'home')
]