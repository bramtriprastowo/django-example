from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello World</h1>')
    context = {
        'name': 'Patrick',
        'age': 24
    }
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = 'Booo'
    # feature1.details = 'Detailed Booooo'
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'words': words, 'amount_of_words': amount_of_words})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('register')
        else:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html', )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
    
# def post(request, variable):
#     return render(request, 'post.html', {'variable': variable})