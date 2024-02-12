from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def __str__(self):
        return f'{self.username} - Profile'

class Pet(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pets', default=None)
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(null=False)
    image = models.ImageField(
        default='default.jpg', upload_to='pet_images')
    gender = models.CharField(max_length=20, blank=False, null=False)
    specie = models.CharField(max_length=20, blank=False, null=False)
    breed = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(null=False)
    size = models.CharField(max_length=20, blank=False, null=False)
    weight = models.FloatField(null=False)
    color = models.CharField(max_length=20, blank=False, null=False)
    availability = models.CharField(max_length=15, blank=False, null=False)
    date_added = models.DateField(null=False)
    location = models.CharField(max_length=50, blank=False, null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.specie} - owned by {self.owner.username}'


class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders_as_customer', default=None)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders_as_seller', default=None)
