from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Question(models.Model):
    question = models.TextField(_("Your Question"))
    
    def __str__(self):
        return self.question
    
    
class Answer(models.Model):
    quetion= models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.CASCADE)
    answer = models.CharField(_("Answer"), max_length=50)
    
    def __str__(self):
        return self.answer
    
class Voters(models.Model):
    voter = models.CharField(_("Voter name"), max_length=50)
    question = models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name=_("Answer"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.voter