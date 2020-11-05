from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, default="No Bio..", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    profile_pic= CloudinaryField('image')
    neighborhood = models.ForeignKey('Neighborhood',on_delete=models.SET_NULL,null=True,blank=True, related_name='tenant')

    def __str__(self):
        return f'{self.user.username} profile'

class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    picture = CloudinaryField('image')
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='landlord')

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

    def update_neighborhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.hood_name}'

class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="owner")
    neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE,related_name='business')
    email = models.EmailField(max_length=225)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self,name):
        self.name = name
        self.save()

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post_editor") 
    neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE,related_name='post')
    posted = models.DateTimeField(auto_now_add=True)