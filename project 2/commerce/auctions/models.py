from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    categories = (('Home', 'Home'), ('Fashion', 'Fashion'),
                  ('Jewellery', 'Jewellery'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Other', 'Other'))
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imgURL = models.URLField(blank=True, max_length=200)
    uploadTime = models.DateField("date added", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=categories, blank=True, max_length=14)
    ended = models.BooleanField(default=False)
    winner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="winner")

    def __str__(self) -> str:
        return self.title


class Bid(models.Model):
    added_date = models.DateField(auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing} -> {self.user}({self.value})"


class Comment(models.Model):
    added_date = models.DateField(auto_now_add=True)
    entry = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing} -> {self.user}"


class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing} -> {self.user}"
