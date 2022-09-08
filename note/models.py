from turtle import title
from django.db import models

# Create your models here.
class Note(models.Model):
               title=models.CharField(max_length=255)
               content=models.TextField(max_length=1000)
               create_at=models.DateTimeField(auto_now_add=True)
               def __str__(self):
                              return self.title

               class Meta:
                              db_table = 'Note'
                              managed = True
                              verbose_name = 'Note'
                              verbose_name_plural = 'Notes'