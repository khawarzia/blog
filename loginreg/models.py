from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(null=True,verbose_name='',upload_to='profile_pics')

    def __str__(self):
        return ('Profile of '+self.user.username)