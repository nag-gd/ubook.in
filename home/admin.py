from django.contrib import admin
from .models import Friends, Create_Post


# Register your models here.

class FriendsAdmin(admin.ModelAdmin):
    list_display=['name','profession','organization','working_city','phone', ]



class PostAdmin(admin.ModelAdmin):
    list_display=['title','message', 'posted_time','posted_by',]

admin.site.register(Friends, FriendsAdmin)
admin.site.register(Create_Post, PostAdmin)