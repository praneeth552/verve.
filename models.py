from django.db import models
from django.contrib.auth.models import User

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate the image with a user
    image = models.ImageField(upload_to='user_images/')  # Save images in a specific folder
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Track upload time

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserImage, on_delete=models.CASCADE, related_name='likes')
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserImage, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)