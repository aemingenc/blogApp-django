from django.db import models
from django.utils import timezone
from users.models import User
# from django.conf import settings

 # author = models.ForeignKey(
    #   settings.AUTH_USER_MODEL, 
    #   on_delete=models.CASCADE
    # )
class Post(models.Model):
   
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='post_image', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    CATEGORY_CHOICES = (
        ('Action','ACTİON'),
        ('History', 'HISTORY'),
        ('influential','INFLUENTIAL'),
        
    )
    Category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='Action')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    body =models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  self.post.title