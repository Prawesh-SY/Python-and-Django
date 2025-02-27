from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Seller(models.Model):
    # 1. GENERAL INFORMATION 
    
    # 1.a. SELLER ACCOUNT
    first_name= models.TextField(_("First Name"), max_length=15)
    middle_name= models.TextField(_("Middle Name"), max_length=15)
    last_name= models.TextField(_("Last Name"), max_length=15)
    email= models.EmailField(_("E-mail"), max_length=254)
    mobile_number= models.IntegerField(_("Mobile Number"))
    shop_name= models.TextField(_("Diplay Name/Shop Name"), max_length=100)
    holiday_mode= models.BooleanField(_("Holiday Mode"), default=False)
    holiday_start= models.DateField(_("Holiday Starts from"), auto_now=False, auto_now_add=False)
    holiday_end= models.DateField(_("Holiday Ends on"), auto_now=False, auto_now_add=False)
    # 1.b. BUSINESS INFORMATION
    seller_type= models.TextField(_("Seller Type"), max_length=50)  # Need to modify to accept one from given option
    legal_name= models.TextField(_("Legal Name/ Business Owner Name"), max_length=100)
    business_address= models.TextField(_("Business Address"), max_length=100)
    business_city= models.TextField(_("City"))
    
    homepage= models.URLField(_("Seller Hompage"), max_length=200)
    
    
    # password= models.PasswordField(_("Password:"), max_length= 24)