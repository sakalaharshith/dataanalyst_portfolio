from django.db import models
from django.contrib.auth.models import User #This is a predefined user model created when a user is created through admin panel.
from django.utils.html import format_html

# Creating Database Model just for images to display in the admin panel and portfolio
class Image(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to='images/')

# Creating database model to populate education section in the portfolio
class Education(models.Model):
    UniversityName=models.CharField(max_length=200)
    ResultDate=models.CharField(max_length=200,default='')
    CourseName=models.CharField(max_length=800)
    extras=models.CharField(max_length=200,default='')
    content=models.TextField()

    def __str__(self):
        return self.UniversityName

class WorkExperience(models.Model):
    CompanyName=models.CharField(max_length=300,default='')
    JobDate=models.CharField(max_length=400,default='')
    JobResponsibilities=models.TextField()
    TechnologiesUsed=models.TextField()

    def __str__(self):
        return self.CompanyName

class Projects(models.Model):
    ProjectName=models.CharField(max_length=400,default='')
    ProjectDescription=models.TextField()
    TechnologiesUsed=models.TextField()
    ProjectImage=models.ImageField(null=True,blank=True,upload_to='images/')
    
    def __str__(self):
        return self.ProjectName
    
class articles_certification_accomplishments(models.Model):
    title=models.CharField(max_length=400,default='')
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    link=models.URLField(max_length=400,blank=True,null=True,default='#')
    
    def __str__(self):
        return self.title


'''
To view sql code implemented or generated whenever a new model and its records are created underhood by django
By default we have used sqlite database but we can use MYSQL, Postgresql etc...
command to type is: python manage.py sqlmigrate {appname} {migrationname} 
ex: python manage.py sqlmigrate website 0004
output:
CREATE TABLE "new__website_education" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "extras" varchar(200) NOT NULL, "UniversityName" varchar(200) NOT NULL, "CourseName" varchar(800) NOT NULL, "content" text NOT NULL, "ResultDate" varchar(200) NOT NULL);
INSERT INTO "new__website_education" ("id", "UniversityName", "CourseName", "content", "ResultDate", "extras") SELECT "id", "UniversityName", "CourseName", "content", "ResultDate", '' FROM "website_education";
DROP TABLE "website_education";
ALTER TABLE "new__website_education" RENAME TO "website_education";




'''