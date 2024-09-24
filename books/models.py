from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE = (
        ('fantasy', 'fantasy'),
        ('sci-fi', 'sci-fi'),
        ('horror', 'horror'),
        ('thriller', 'thriller'),
        ('detective', 'detective'),
        ('romance', 'romance'),
        ('classics', 'classics'),
        ('philosophy', 'philosophy'),
        ('history', 'history'),
        ('religion', 'religion'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books_images', null=True, blank=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    publisher_email = models.EmailField(verbose_name='Enter the publisher`s email address')
    is_bestseller = models.BooleanField(default=False, verbose_name='Bestseller')

    def __str__(self):
        return f"{self.title} - {self.author}"

