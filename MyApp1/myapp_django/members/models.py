from django.db import models

class Member(models.Model):
  id = models.IntegerField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  joined_date = models.DateField(blank=True, null=True)
  phone = models.CharField(max_length=20, blank=True, null=True)
  married = models.BooleanField(default=True, blank=True, null=True)
  slug = models.SlugField(default="",null=False)
#   slug_hash = models.CharField(max_length=8, default=generate_slug_hash, null=False)
#   slug = models.SlugField(default="", null=False)

def __str__(self):
  return f'{self.firstname} {self.lastname}'

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50 , null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50,  null=True)
    email = models.EmailField (max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)

def __str__(self):
  return f'{self.username} {self.password}'

#in html date_field = forms.DateField(required=False) 