from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse  # Import reverse for get_absolute_url


# Create your models here.
class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=15, decimal_places=2)
    updated_price = models.DecimalField(_("Updated Price"), max_digits=15, decimal_places=2, blank= True, null= True)
    stock = models.PositiveIntegerField(_("Units in Stock"), null=False)
    expiry_date = models.DateField(_("Expiry Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    is_available = models.BooleanField(_("Is Available"), default=True)
    image = models.ImageField(_("Upload Prodcut Image"), upload_to="product/images", height_field=None, width_field=None, max_length=None)
    category = models.CharField(_("Category"), max_length=50, choices=[('PC','PC'), ('Clothes','Clothes')])
    made_in = models.CharField(_("Country of Origin"), max_length=50)
    brand = models.CharField(_("Brand"), max_length=50)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

class PC(Product):
    usb_count = models.PositiveIntegerField(_("Total USB Ports"))
    special_features = models.TextField(_("Special Features"), max_length=240)
    cellular_tech = models.CharField(_("Cellular Technology"), max_length=50)
    memory_type = models.CharField(_("MEMORY type"), max_length=50)
    memory_size = models.CharField(_("MEMORY size"), max_length=50)
    graphics_type = models.CharField(_("Graphics Description"), max_length=50)
    graphics_memory = models.CharField(_("Dedicated Graphics Memory"), max_length=50)
    graphics_interface = models.CharField(_("Graphics Card Interface"), max_length=100)
    vid_op_interface = models.CharField(_("Video Output Interface"), max_length=50)
    vid_op_count = models.PositiveIntegerField(_("Total Video Output Ports"))
    wirless_tech = models.TextField(_("Wireless Communication Standards"))
    input_interface = models.TextField(_("Human Input Interface"))
    screen_size = models.PositiveIntegerField(_("Screen Size(in inches)"))
    components = models.TextField(_("Included Components"))
    operating_system = models.CharField(_("Operating System"), max_length=150)
    cpu_count = models.PositiveIntegerField(_("Processor Count"))
    cpu_type = models.CharField(_("Processor Type"), max_length=100)
    cpu_series = models.CharField(_("Processor Series"), max_length=50)
    cpu_clock = models.CharField(_("Processor Speed"), max_length=50)
    cpu_socket = models.CharField(_("CPU Socket"), max_length=50)
    resolution = models.CharField(_("Resolution"), max_length=50)
    connectivity = models.TextField(_("Connectivity Technology"))
    use_case = models.TextField(_("Specific Uses of Product"))
    storage_type = models.CharField(_("Storage type"), max_length=50)
    storage_size = models.CharField(_("Storage size"), max_length=50)
    color = models.CharField(_("Color"), max_length=50)
    
    class Meta:
        verbose_name =_("PC")
        verbose_name_plural = _("PCs")
        
    def __str__(self):
        return f"PC: {self.brand}"
    
class Clothes(Product):
    color = models.CharField(_("Color"), max_length=50)
    
    class Meta:
        verbose_name = _("Cloth")
        verbose_name_plural = _("Clothes")
        
class Men(Clothes):
    TYPE_CHOICES = [
        ('Topwear', 'Topwear'),
        ('Bottomwear', 'Bottomwear'),
        ('Footwear', 'Footwear'),
        ('Sports & Active wear', 'Sports & Active wear'),
        ('Fashion Accessories', 'Fashion Accessories'),
        ('Ethnic & Festive wear', 'Ethnic & Festive wear'),
        ('Innerwear & Sleepwear', 'Innerwear & Sleepwear'),
        ('Personal Care & Grooming', 'Personal Care & Grooming'),
        ('Sunglasses & Frames', 'Sunglasses & Frames'),
        ('Watches', 'Watches'),
        ('Gadgets', 'Gadgets'),
        ('Bags & Backpacks', 'Bags & Backpacks'),
        ('Luggages & Trolleys', 'Luggages & Trolleys'),
    ]
    type = models.CharField(_("Type"), max_length=50, choices= TYPE_CHOICES)
    size = models.CharField(_("Size"), max_length=50)
    fitting = models.CharField(_("Body Fitting"), max_length=50)
    

class Category(models.Model):
    name = models.CharField(_("Category"), max_length=111, choices=(("Electronics", 'Electronics'),("Clothes", 'Clothes')))
    main_category = """This should have data as per the cases:
                        Case 1: When the data is the main category like Clothes, Electronics
                                main_category = null
                        Case 2: When the data is the sub-category to a main category like sub-category: Male of main cagetgory: Clothes
                                main_category = <id of Clothes>


    """
    
    class Meta:
        verbose_name = _("Category") 
        verbose_name_plural = _("Categories")
          
    def __str__(self):
        return self.name

class Productasperhtml(models.Model):
     name = models.CharField(_("Name"), max_length=255)
     des = models.TextField(_("Description"))
     category = models.ForeignKey(Category, verbose_name=_("Category"), related_name='category', on_delete=models.CASCADE)
     price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
     updated_price = models.DecimalField(_("Updated Price"), max_digits=10, decimal_places=2, null= True, blank= True)
     stock = models.PositiveIntegerField(_("Units In Stock"))
     units_sold = models.PositiveIntegerField(_("Units Sold"), null= True, blank= True)
     image = models.ImageField(_("Product Image"), upload_to="product/images", height_field=None, width_field=None, max_length=None)
     
     def __str__(self):
        return self.name
     
