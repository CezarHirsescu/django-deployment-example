from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# this model is different from the user
# the user is builtin to django, we are creating a different model here
class UserProfileInfo(models.Model):
    # adding a user attribute is better than inheriting from the user class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # other stuff you want your user to have
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
