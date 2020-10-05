from django.db import models
from django.conf import settings
# from django.utils.timezone import now as utcnow


class Friends(models.Model):
    name = models.CharField(max_length=32)
    profession = models.CharField(max_length=64)
    organization = models.CharField(max_length=64)
    working_city = models.CharField(max_length=32)
    phone = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'home_friends'

class Create_Post(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    message=models.TextField(blank=False)
    posted_time=models.DateTimeField(auto_now_add=True,)
    posted_by =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    


    class Meta:
        managed = True
        db_table = 'home_posts'


