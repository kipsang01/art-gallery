from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.location1 = Location(name ='Nairobi')
        self.category1 = Category(category = 'Nature')
        self.image1= Image(image = 'mountain.jpg',name = 'Mountain', location = self.location1, category = self.category1)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location1,Location))
        self.assertTrue(isinstance(self.category1,Category))
        self.assertTrue(isinstance(self.image1,Image))
        
    # Testing Save Method
    def test_save_method(self):
        self.location1.save_location()
        self.category1.save_category()
        self.image1.save_image()
        images = Image.objects.all()
        categories = Category.objects.all()
        locations = Location.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(categories) > 0)
        self.assertTrue(len(locations) > 0)
     
      # Testing Delete Method   
    def test_delete(self):
        self.location1.save_location()
        self.category1.save_category()
        self.image1.save_image()
        Image.objects.get(id =self.image1.id).delete()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
       
       # Testing Get Image by Id 
    def test_get_image_by_id(self):
        self.location1.save_location()
        self.category1.save_category()
        self.image1.save_image()
        image = Image.get_image_by_id(self.image1.id)
        self.assertTrue(image is not None)
        
        # Testing Update image
        
    def test_update_image(self):
        self.location1.save_location()
        self.category1.save_category()
        self.image1.save_image()
        image = Image.get_image_by_id(self.image1.id)
        image.update_image('peak.jpg')
        image = Image.get_image_by_id(self.image1.id)
        self.assertTrue(image.image == 'peak.jpg')