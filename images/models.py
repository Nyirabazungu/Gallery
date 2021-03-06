from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length =40)
   
 
    

    def __str__(self):
        return self.category

    # class Meta:
    #     ordering = ['category']


    def save_images(self):
         self.save()  
         
    def delete_images(self):
         self.save()  

    def display_images(self):
         self.save()

    def update_images(self):
         self.save()    

    

class Location(models.Model):
    country = models.CharField(max_length =30)
 


    def __str__(self):
        return self.country  

     
    def save_images(self):
         self.save()  
         
    def delete_images(self):
         self.save()  

    def display_images(self):
         self.save()

    def update_images(self):
         self.save()       

class Image(models.Model):
    title = models.CharField(max_length =70)
    description= models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    images= models.ImageField(upload_to = 'images/')
   

    def __str__(self):
        return self.title

      

    def save_images(self):
         self.save()  
         
    def delete_images(self):
         self.save()  

    def display_images(self):
         self.save()

    def update_images(self):
         self.save()     

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images
 
       



    







    
