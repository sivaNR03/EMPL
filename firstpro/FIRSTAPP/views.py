from django.shortcuts import render,HttpResponse, redirect
from .models import Employee
def user_sigin(request):
    if request.method == "POST":
       user_name =request.POST["username"]
       user_gmail = request.POST["gmail"]
       user_password = request.POST["password"]
       user_confrmpassword = request.POST["confrmpassword"]
       if user_password != user_confrmpassword:
        return HttpResponse("password does not match")
       else:
        user = Employee(username=user_name,gmail=user_gmail,password=user_password,confrmpassword=user_confrmpassword)
        user.save()
        return redirect(user_login)
    return render(request,"regist.html")

def user_login(request):
    if request.method == "POST":
       username =request.POST["username"]
       password = request.POST["password"]
       user_details = Employee.objects.all()
       user = None
       for user in user_details:
        if(user.username,user.password)==(username,password):
            user = user.username
            request.method = " "
            break
       if user is not None:
          return redirect (home_page)
       else:
          return HttpResponse("invalid details")
    return render(request,"login.html")

def home_page(request):
   if request.method == "POST":
    return redirect(user_login)
   return render(request,"home.html")
    

                    

