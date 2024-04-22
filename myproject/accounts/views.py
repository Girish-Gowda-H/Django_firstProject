from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    print(f"user : {User.objects}")
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(first_name=first_name).exists():
                messages.info(request,'first name taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, first_name = first_name)
                user.save()
                print('user created') 
                return redirect('login')  
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')