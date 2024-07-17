from django.shortcuts import render, redirect
from .models import Receipe  # Ensure you import the Receipe model correctly
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image') 
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            receipe_description=receipe_description  
        )
        
        # After saving the new recipe, fetch all recipes again for display
        receipes = Receipe.objects.all()
        context = {'receipes': receipes}
        return render(request, 'receipes.html', context)
    
    # If the request method is not POST (i.e., it's GET), display the form
    else:
        receipes = Receipe.objects.all()
        context = {'receipes': receipes}
        return render(request, 'receipes.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(user)
            return redirect('/receipes/')


    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        user = User.objects.create(
            first_name=first_name,
            username=username,
            email=email
        )
        
        user.set_password(password)
        user.save()
        
        return redirect('login')  # Redirect to the login page after registration
    
    else:
        return render(request, 'register.html')
