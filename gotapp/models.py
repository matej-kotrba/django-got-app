from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name", help_text="Enter a name of character")
    description = models.TextField()

    class Meta:
        verbose_name = "Jméno"
        verbose_name_plural = "Jména"
        ordering = ['name']

    def __str__(self):
        return self.name