from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    rating_choice = (
        ("1", "⭐"),
        ("2", "⭐⭐"),
        ("3", "⭐⭐⭐"),
        ("4", "⭐⭐⭐⭐"),
        ("5", "⭐⭐⭐⭐⭐"),
    )
    genre_choice = (
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Horror", "Horror"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
        ("Thriller", "Thriller"),
        ("Sci-fi", "Sci-fi"),
        ("Others", "Others"),
    )

    title = models.CharField(max_length=80)
    content = models.TextField()
    grade = models.CharField(max_length=20, choices=rating_choice)
    genre = models.CharField(max_length=80, choices=genre_choice)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/movies", blank=True)
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(295, 295)],
        format="JPEG",
        options={"quality": 80},
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
