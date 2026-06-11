from django.db import models
from django.contrib.auth.models import User


class EBook(models.Model):

    CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Fiction', 'Fiction'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=100)

    summary = models.TextField()

    pages = models.IntegerField()

    pdf = models.FileField(upload_to="pdfs/")

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title