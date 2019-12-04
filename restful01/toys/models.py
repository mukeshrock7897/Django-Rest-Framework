from django.db import models

# Create your models here.

class Toy(models.Model):
    created = models.DateTimeField(verbose_name="created",auto_now_add=True,editable=True)
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=100)
    toy_category = models.CharField(max_length=100)
    release_date = models.DateTimeField(verbose_name="release_date",auto_now=True)
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering=("created",)
    
    def __str__(self):
        return '{} {} {}'.format(self.name , self.toy_category , self.created)

