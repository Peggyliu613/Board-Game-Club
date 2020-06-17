from django.db import models
import re
import bcrypt

class UsersManager(models.Manager):
    
    def validator(self, postdata):
        errors={}
        if not postdata['first_name'] and len(postdata['first_name'])<2 or not postdata['first_name'].isalpha():
            errors['first_name']="First name should be at least 2 characters"
        if not postdata['last_name'] and len(postdata['last_name'])<2 or not postdata['last_name'].isalpha():
            errors['last_name']="Last name should be at least 2 characters"
        if not re.search(".+@.+\..+", postdata['email']):
            errors['email']="invalid email"
        if not postdata['password'] or len(postdata['password'])<6:
            errors['password']="Password should be at least 6 characters"
        if postdata['password']!=postdata['confirmpassword']:
            errors['confirmpassword']="Password does not matched"
        is_email_exit=Users.objects.filter(email=postdata['email'])
        if len(is_email_exit)>0:
            errors['email']="Email is used"
        return errors

    def validator_login(self, postdata):
        errors={}
        try: 
            the_user=Users.objects.get(email=postdata['email'])
            if not bcrypt.checkpw(postdata['password'].encode(), the_user.password.encode()):
                errors['password']="Email/Password does not matched"
            return errors
        except:
            errors['email']="Email/Password does not matched"
            return errors
    
class EventsManager(models.Manager):
    def validator(self, postdata):
        errors={}
        if len(postdata['title'])<3:
            errors['title']="Title should be at least 3 characters"
        if len(postdata['desc'])<3:
            errors['desc']="Description should be at least 3 characters"
        if not postdata['location']:
            errors['location']="A location must be provided"
        return errors


class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #events_created
    #events_joined

    objects=UsersManager()

class Events(models.Model):
    name=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TextField()
    location=models.CharField(max_length=255)
    desc=models.TextField(null=True)
    created_by=models.ForeignKey(Users, related_name="events_created", on_delete=models.CASCADE)
    joined_by=models.ManyToManyField(Users, related_name="events_joined", null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    objects=EventsManager()

class Werewolf_Characters(models.Model):
    character=models.CharField(max_length=255)
    function=models.CharField(max_length=255)
    # number_of_players=models.CharField(max_length=1)
    is_using=models.BooleanField(default=False)

class Avalon_Characters(models.Model):
    character=models.CharField(max_length=255)
    function=models.CharField(max_length=255, null=True)
    is_using=models.BooleanField(default=False)


class Players(models.Model):
    name=models.CharField(max_length=255)
    order_number = models.IntegerField(null=True)