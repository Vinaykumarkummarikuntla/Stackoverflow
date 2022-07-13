from distutils.command.upload import upload
from email.mime import image
from django.forms import CharField, ImageField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User


class Question(models.Model):
    userid = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    # content = models.TextField(null=True, blank=True)
    content = RichTextField()
    #likes = models.ManyToManyField(User, related_name='question_post')
    date_created = models.DateTimeField(default=timezone.now)   
    
    # def __str__(self):
    #     return f'{self.user.username} - Question'
    
    # def get_absolute_url(self):
    #     return reverse('stackbase:question-detail', kwargs={'pk':self.pk})
    
    # def total_likes(self):
    #     return self.likes.count()

class Comment(models.Model):
    #userid = models.ForeignKey(user, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)   

    # def __str__(self):
    #     return '%s - %s' % (self.question.title, self.question.user)

    # def get_success_url(self):
    #     return reverse('stackbase:question-detail', kwargs={'pk':self.pk})
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

class user(models.Model):
    username = models.OneToOneField("user", on_delete=models.CASCADE)
    bio = CharField()
    phonenumber = models.IntegerField()
   # image =  ImageField(upload= " ")

