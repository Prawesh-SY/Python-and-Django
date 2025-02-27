from django.db import models
from django.utils.translation import gettext_lazy as _
from django. urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Agency(models.Model):
    agency_name = models.CharField(_("Agency Name"), max_length=254)
    role = models.CharField(_("Role in Agency"), max_length=254)
    agency_email = models.EmailField(_("Agency Email Address"), max_length=254)
    agency_website = models.URLField(_("Website"), max_length=200)
    agency_address = models.TextField(_("Address"))
    region = models.CharField(_("Region of Operation"), max_length=111)

class Service(models.Model):
    # Model to hold multiple Services that the candidate can provide
    services = models.CharField(_("Services Provided"), max_length=50, choices=[(1, 'Career Counseling'), (2, 'Admission Applications'), (3, 'Visa Processing'), (4, 'Test Preparation')])
    pass
class Country(models.Model):
    # Model to hold preferred countries of operation
    countries = models.CharField(_("Preferred Countries"), max_length=121)
    pass
class Institution(models.Model):
    institutions = models.CharField(_("Preferred Institution Types"), choices=[(1, 'Universities'), (2, 'Colleges'), (3, 'Vocational School'),(4, 'Others')], max_length=50)
    # Model to hold multiple Preferred Instituion Types
    pass
class BusinessDoc(models.Model):
    # Model to hold multiple Business Documents
    doc= models.FileField(_("Upload Business Documents"), upload_to='seller/documents', max_length=100)
    

class Experience(models.Model):
    years = models.PositiveIntegerField(_("Years of Experience"))
    student_count = models.PositiveIntegerField(_("Number of Students Reqruited Annually"))
    focus_area = models.TextField(_("Focus Area"))
    success_metrics = models.DecimalField(_("Success Metrics"), max_digits=3, decimal_places=2)
    services = models.ForeignKey(Service, verbose_name=_("Services Provided"), related_name='service', on_delete=models.CASCADE)
    
class Preference(models.Model):
    business_reg_number = models.CharField(_("Business Registration Number"), max_length=150)
    country =  models.ForeignKey(Country, related_name="country", verbose_name=_(""), on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, related_name= 'instiution', verbose_name=_("Preferred Institution Types"), on_delete=models.CASCADE)
    certification = models.CharField(_("Certification Details"), max_length=150)
    doc = models.ForeignKey(BusinessDoc, verbose_name=_("Upload Business Documents"), related_name='business_doc', on_delete=models.CASCADE)
    
class Seller(models.Model):
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    email = models.EmailField(_("Email Address"), max_length=254)
    phone_number = PhoneNumberField(_("Phone Number"))
    password = models.CharField(_("Password"), max_length=254)
    agency = models.ForeignKey(Agency, verbose_name=_("agency Details"), related_name='agency', on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, verbose_name=_("Experience and Performance Metics"), related_name="experience", on_delete=models.CASCADE)
    
    