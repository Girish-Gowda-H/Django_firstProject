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
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')