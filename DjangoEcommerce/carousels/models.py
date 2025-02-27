from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Carousel(models.Model):
    des = models.TextField(_("Description"), max_length=240, default=None)
    image = models.ImageField(_("Display banner"), upload_to='carousels/images/', height_field=None, width_field=None, max_length=None, default=None)
    created_on = models.DateTimeField(_("Created on"), auto_now=False, auto_now_add=False, default= None)
    displayed_from = models.DateField(_("To be displayed from"))
    displayed_to = models.DateField(_("To be displayed till"))
    is_active = models.BooleanField(default=True)