from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from .models import FeedBack,Contact,User

from django.views.decorators.cache import cache_control

from django.contrib import messages

def home(request):
    feedback_list=FeedBack.objects.order_by('-date')[:6]#select*from feedback orderby date desc
    context={"feedback_key":feedback_list}#created a dictionary
    return render(request,'vocal_app/html/index.html',context)#send it on index.html

def about(request):
    return  render(request,'vocal_app/html/about_us.html')

def contact(request):
    if request.method=="GET":##Http Protocol method
     return render(request,'vocal_app/html/contact_us.html')
    
    if request.method=="POST":
         nm=request.POST["u_name"]#request.POST is builtIndict fetch the values from control
         em=request.POST["u_email"]
         ph=request.POST["u_phone"]
         qu=request.POST["u_question"]

         contact_obj=Contact(name=nm,email=em,phone=ph,question=qu)#object of feedback model
         contact_obj.save()#object save->it will map data with table column
         messages.success(request,"Thank you for contacting us..Soon we will give response")
         return render(request,'vocal_app/html/contact_us.html')


def user_feedback(request):
    if request.method=="GET":##Http Protocol method
       return render(request,'vocal_app/user/user_feedback.html')
      
    if request.method=="POST":
         nm=request.POST["u_name"]#request.POST is builtIndict fetch the values from control
         em=request.POST["u_email"]
         rt=request.POST["rating"]
         rw=request.POST["u_review"]
         pic=request.session["st_pic"]
         feedback_obj=FeedBack(name=nm,email=em,rating=rt,reviews=rw,pic=pic)#object of feedback model
         feedback_obj.save()#object save->it will map data with table column
         messages.success(request,"Thank you for your feedback")
         return render(request,'vocal_app/user/user_feedback.html')

def user_login(request):
  if "session_key" in request.session.keys():
      if request.method=="GET":
         user_email=request.session["session_key"]
         user_obj=User.objects.get(email=user_email)
         context={
            "user_key":user_obj
         }
      

         return redirect("user_home")
  if request.method=="GET":
    return render(request,'vocal_app/user/user_login.html')
  if request.method=="POST":
    em=request.POST["user_email"]
    pwd=request.POST["user_pass"]
    user_list=User.objects.filter(email=em,password=pwd)
    if len(user_list)>0:
    #    user_obj=user_list[0]
    ##    session creation and binding email in that session to identify user request##
       request.session["session_key"]=em ##request.session is a dict
       request.session["st_pic"]=user_list[0].profile_pic.url
       return redirect("user_home")
    else:
       messages.error(request,"Invalid Credentials")
       return redirect("user_login")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True) 

def user_dashboard(request):
  if "session_key" in request.session.keys():
   user_email=request.session["session_key"]
   user_obj=User.objects.get(email=user_email)
   context={
         "user_key":user_obj
   }

   return render(request,"vocal_app/user/user_home.html",context)
  else:
     return redirect("user_login")



def user_edit_profile(request):
  if "session_key" in request.session.keys():
   if request.method=="GET":
    user_email=request.session["session_key"]
    user_obj=User.objects.get(email=user_email)
    context={
         "user_key":user_obj
         }
    return render(request,'vocal_app/user/user_edit_profile.html',context)
   if request.method=="POST":
      user_email=request.session["session_key"]
      user_obj=User.objects.get(email=user_email)
      ##update student set name=nm,phone=ph,address=add where email=user_email
      nm=request.POST["u_name"]
      ph=request.POST["u_phone"]
      add=request.POST["u_address"]
      user_obj.name=nm
      user_obj.phone=ph
      user_obj.address=add
      user_obj.save()#it will modify the old object with new values
      messages.success(request,"Profile Updated Successfully")
      return redirect("user_home")
  else:
      return redirect("user_login")

def user_registration(request):
    
    if request.method=="GET":
     return render(request,'vocal_app/user/user_registration.html')
    
    if request.method=="POST":
         file_name=request.FILES.get("u_file")
         name=request.POST["u_name"]#request.POST is builtIndict fetch the values from control
         email=request.POST["u_email"]
         phone=request.POST["u_phone"]
         address=request.POST["u_address"]
         password=request.POST["u_password"]

         obj=User(name=name,email=email,password=password,phone=phone,address=address,profile_pic=file_name)
         obj.save()

         return render(request,'vocal_app/user/user_login.html')
    
    ###student_logout##

def user_logout(request):
   del request.session["session_key"]#delete the session
   return redirect("user_login")

def voice_notes(request):
 if "session_key" in request.session.keys():
   return render(request,"vocal_app/user/voice_notes.html")
 else:
      return redirect("user_login")

def read_notes(request):
 if "session_key" in request.session.keys(): 
   return render(request,"vocal_app/user/read_notes.html")
 else:
      return redirect("user_login")