from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name", help_text="Enter a name of place")
    image = models.ImageField(upload_to='places', verbose_name="Image", help_text="Upload a image of place")
    description = models.TextField(max_length=500, verbose_name="Description", help_text="Enter a description of place")

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name", help_text="Enter a name of house")
    region = models.CharField(max_length=50, verbose_name="Region", help_text="Enter a region of house")
    coat_of_arms = models.ImageField(null=True, verbose_name="Coat of Arms", help_text="Upload a coat of arms of house")
    words = models.CharField(max_length=50, verbose_name="Words", help_text="Enter a words of house")
    home = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name="Home", help_text="Select a home of house")

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Character(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name", help_text="Enter a name of character")
    actor = models.CharField(max_length=80, verbose_name="Actor", help_text="Enter a name of actor", null=True)
    first_episode = models.CharField(max_length=50, verbose_name="First Episode", help_text="Enter a first episode where character appears", null=True)
    image = models.ImageField(upload_to='characters', verbose_name="Image", help_text="Upload a image of character", null=True)
    description = models.TextField(null=True)
    house = models.ManyToManyField(House, verbose_name="House", help_text="Select a house of character")

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ['name']

    def __str__(self):
        return self.name
