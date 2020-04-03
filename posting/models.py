from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,blank=True)
    text = models.TextField(max_length=2000,blank=True)
    picture = models.ImageField(null=True,verbose_name='Attach a picture',upload_to='post-images')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title