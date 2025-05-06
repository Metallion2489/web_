from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='pelmeni_images/')

    def __str__(self):
        return self.name

class Review(models.Model): 
    title = models.CharField(max_length=200)
    body = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
    
