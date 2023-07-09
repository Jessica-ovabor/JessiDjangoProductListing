#defining the app urls
from django.urls import path
from app.views import main_view

urlpatterns = [
    
    path('',main_view,name='app'),
    
]