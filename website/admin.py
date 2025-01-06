from django.contrib import admin
from .models import Image,Education,WorkExperience,Projects,articles_certification_accomplishments

#Registering the database models to the admin interface
admin.site.register(Image)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Projects)
admin.site.register(articles_certification_accomplishments)


