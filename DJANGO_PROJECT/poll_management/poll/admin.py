from django.contrib import admin
from . models import Question, Answer, Voters
# Register your models here.
admin.site.register([Question, Answer, Voters])