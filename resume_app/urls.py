from django.urls import path, include
from resume_app.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name= 'home')
]