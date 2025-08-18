from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Tweet(models.Model):
    """
    Tweet model representing a user's post with optional photo attachment.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(
        max_length=280,
        validators=[
            MinLengthValidator(1, message="Tweet cannot be empty"),
            MaxLengthValidator(280, message="Tweet cannot exceed 280 characters")
        ]
    )
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'