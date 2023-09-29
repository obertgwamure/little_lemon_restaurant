from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# generating unique file names for image uploads
def post_image_path(instance, filename):
    filename = os.path.basename(slugify(filename))  # remove any directory paths from filename
    return (f'img/{instance.id or 1}/{filename}')

class Menu(models.Model):
   name = models.CharField(max_length=200)
   description = models.TextField()
   image = models.ImageField(upload_to='post_image_path', blank=True)
   price = models.FloatField()

   class Meta:
      ordering = ('name',)

   def __str__(self):
      return str(self.title)
    
   def get_absolute_url(self):
      return reverse('restaurant:menu_item', kwargs={'pk': self.pk})
    