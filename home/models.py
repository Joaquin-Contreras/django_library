from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    bio = models.TextField()

class comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True),
    user_id = models.ForeignKey(user,on_delete=models.CASCADE),
    content = models.TextField(),
    date_posted = models.DateTimeField(auto_now_add=True),
    approved_comment = models.BooleanField(default=False)

class rents(models.Model):
    rent_id = models.BigAutoField(primary_key=True),
    user_id = models.ForeignKey(user, on_delete=models.CASCADE),
    title = models.CharField(max_length=200),
    description = models.TextField(),
    price = models.DecimalField(decimal_places=10, max_digits=15),
    location = models.CharField(max_length=300),
    published_date = models.DateTimeField(auto_now_add=True),
    status = models.BooleanField(),
    reviews_nb = models.DecimalField(decimal_places=10, max_digits=20),
    reviews_avg = models.DecimalField(decimal_places=5, max_digits=20),
    comments = models.ForeignKey(comments, on_delete=models.CASCADE),
    bedrooms = models.DecimalField(decimal_places=4 ,max_digits=15),
    bethrooms = models.DecimalField(decimal_places=4 ,max_digits=15),
    total_guests_limit = models.DecimalField(decimal_places=4 ,max_digits=15)









