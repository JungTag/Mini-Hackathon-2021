from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(request, username=username, password=password)
    
    if user is not None:
      auth.login(request, user)
      return redirect('main')
    
    else:
      msg = "아이디 혹은 비밀번호가 일치하지 않습니다."
      return render(request, "login.html", {"msg" : msg})
    
  return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    username = request.POST['username']
    
    if password1 == password2:
      try:
        user = User.objects.get(username=usernmae)
        msg = "이미 사용중인 아이디입니다."
        return render(request, 'signup.html', {'msg' : msg})
      
      except User.DoesNotExist:
        user = User.objects.create_user(
          username = request.POST['username'],
          password = request.POST['password1'],
          email = request.POST['email_address'],
          )
        user.save()
        
        msg = "회원가입이 완료되었습니다. 다시 로그인해주세요."
        return render(request, 'login.html', {'msg' : msg})
    
    else:
      msg = "비밀번호가 일치하지 않습니다."
      return render(request, 'signup.html', {'msg' : msg})

  
  return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('account:login')