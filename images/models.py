from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length =30)
 
    

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']

class Location(models.Model):
    country = models.CharField(max_length =30)
 


    def __str__(self):
        return self.country  

class Images(models.Model):
    title = models.CharField(max_length =60)
    description= models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    images_images = models.ImageField(upload_to = 'images/') 

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']     

    def save_images(self):
         self.save()  
         
    def delete_images(self):
         self.save()  

    def display_images(self):
         self.save()

    def update_images(self):
         self.save()     

@classmethod
def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images
 
       