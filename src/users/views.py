from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views import View


# Create your login views here.

def login_view(request):
    if request.method == "POST":
       login_form = AuthenticationForm(request=request, data=request.POST)
       if login_form.is_valid():
           username = login_form.cleaned_data.get("username")
           password = login_form.cleaned_data.get("password")
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request,user)
               messages.success(request, f" You are logged in as {username}")
               return redirect('home')
           else:
               messages.error(request, f"An error occured trying to login.")
       else:
           messages.error(request, f"An error occured trying to login.")
               
    elif request.method == "GET":
        login_form = AuthenticationForm()
    return render(request, 'login.html',{'login_form':login_form})
# def register_view(request):
#     register_form = UserCreationForm()
#     return render(request, 'register.html',{'register_form' :register_form})

#Class based view for register_view is used when you want to perform multiple http request

class RegisterView(View):
    def get(self , request):
        register_form = UserCreationForm()
        return render(request, 'register.html',{'register_form' :register_form})
    def post(self , request):
        register_form = UserCreationForm( data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request,user)
            messages.success(request, f"User {user.username} registered successfully.")
            return redirect('home')
        else:
           messages.error(request, f"An error occured trying to register.")
           return render(request, 'register.html',{'register_form' :register_form})
            
        
        
    