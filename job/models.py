from django.db import models
from django.db.models.fields import URLField
from django.utils.text import slugify
from django.contrib.auth.models import User
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name 


class Job (models.Model):  #table

    owner = models.ForeignKey(User, verbose_name=("Job_owner"), on_delete=models.CASCADE,related_name="owner")
    title = models.CharField(max_length=100) #column 
    

    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0) 
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,default="unknown") 
    image = models.ImageField(upload_to=image_upload)


    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):
    job = models.ForeignKey("Job", related_name=("aplly_job"), on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email  = models.EmailField(max_length=100)
    creat_at = models.DateTimeField(auto_now=True)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name


    
