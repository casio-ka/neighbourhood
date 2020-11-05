from django.contrib import admin
from .models import Neighborhood, Post,Profile,Business

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Business)