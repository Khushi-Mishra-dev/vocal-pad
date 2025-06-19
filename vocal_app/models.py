from django.db import models

from django.utils import timezone

##contact model
class Contact(models.Model):##inheriting Model class in Contact

 name=models.CharField(max_length=45)
 email=models.EmailField(max_length=45)
 phone=models.CharField(max_length=45)
 question=models.TextField()
 date=models.DateField(default=timezone.now)
 def __str__(self): #it is used to represent object in string form
   return self.name

 ##Feedback Model##
class FeedBack(models.Model):
  name=models.CharField(max_length=45)
  email=models.EmailField(max_length=45)
  rating=models.CharField(max_length=5)
  reviews=models.TextField()
  date=models.DateField(default=timezone.now)
  pic=models.CharField(max_length=100,default="")
  def __str__(self): #it is used to represent object in string form
   return self.name

  ##User registration model

class User(models.Model):
   name=models.CharField(max_length=45)
   email=models.EmailField(max_length=55,primary_key=True)
   password=models.CharField(max_length=12)
   phone=models.CharField(max_length=12,default="")
   address=models.TextField()
   profile_pic=models.ImageField(upload_to='test_app/profile_pic',default="")
   def __str__(self): #it is used to represent object in string form
    return self.name
   



