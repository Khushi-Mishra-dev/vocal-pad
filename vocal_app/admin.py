from django.contrib import admin

from.models import Contact,FeedBack,User

class FeedBack_Admin(admin.ModelAdmin):

    list_display=['name','email','rating','reviews']

class Contact_Admin(admin.ModelAdmin):

    list_display=['name','email','phone','question']

class User_Admin(admin.ModelAdmin):

    list_display=['name','email','phone','address']


admin.site.register(Contact,Contact_Admin)
admin.site.register(FeedBack,FeedBack_Admin)
admin.site.register(User,User_Admin)

# Register your models here.
admin.site.site_header="Vocal Admin Dashboard"
admin.site.site_title="Vocal App"
admin.site.index_title="Makes The Work Easier"

