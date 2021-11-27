from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    
    def save_location(self):
        self.save()
        
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def save_category(self):
        self.save()
    
    def __str__(self):
        return self.category
    

class  Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 1000)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    @classmethod
    def image_cat(cls, category):
        images = cls.objects.filter(category__name=category)
        return images
    

