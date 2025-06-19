from django.urls import path
from . import views
urlpatterns = [
  path("",views.home,name="home"), 
  path("about_us/",views.about,name="about"), 
  path("contact_us/",views.contact,name="contact"),
  path("user_feedback/",views.user_feedback,name="user_feedback"),  
  path("user_login/",views.user_login,name="user_login"),  
  path("user_registration/",views.user_registration,name="user_registration"),  
  path("user_dashboard/",views.user_dashboard,name="user_home"),  
  path("user_logout/",views.user_logout,name="user_logout"),  
  path("voice_notes/",views.voice_notes,name="voice_notes"),  
  path("read_notes/",views.read_notes,name="read_notes"),  
  path("user_edit_profile/",views.user_edit_profile,name="user_edit_profile"),  


]
