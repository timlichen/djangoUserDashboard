from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    print "about to render"
    try:
        print request.session['user_id']
    except:
        pass
    return render(request, 'uDash/index.html')

def login(request):
    print "about to render login"
    return render(request, 'uDash/signin.html')

def register(request):
    print "about to render register"
    return render(request, 'uDash/register.html')

def registerUser(request, methods=['POST']):
    print "register a user into db"

    data = {
        "first_name": request.POST['first_name'],
        "last_name": request.POST['last_name'],
        "email": request.POST['email'],
        "password": request.POST['password'],
        "cPassword": request.POST['cPassword']
    }
    theMessage = User.userManager.validator(data)

    if theMessage[0]:
        request.session['user_id'] = theMessage[1]
        return render(request, 'uDash/register.html')
    else:
        data = theMessage[1]
        for message in data:
            print message
            messages.add_message(request, messages.ERROR, data[message])
        return redirect('/register')

def signin(request):
    data = {
        "email": request.POST['email'],
        "password": request.POST['password']
    }
    theMessage = User.userManager.login(data)
    message = dict()
    if theMessage:
        message['success'] = "Sucessfully Logged In!"
        print message['success']
        # return render(request, 'lr_app/signin.html', message)
    else:
        message['failedLogin'] = "Invalid Login"
        print message['failedLogin']
        # return render(request, 'lr_app/signin.html', message)
    return render(request, 'uDash/signin.html')

def adminPanel(request):
    user = User.objects.filter( pk = request.session['user_id'] )
    if int(user[0].auth_level) == 0:
        print "user is an admin"
        all_users = User.objects.all()
        data = {'all_users': all_users}
    return render(request, 'uDash/adminPanel.html', data)

def remove(request, id):
    print id
    return render(request, 'uDash/adminPanel.html', data)

def edit(request, id):
    print id
    return render(request, 'uDash/adminPanel.html', data)
