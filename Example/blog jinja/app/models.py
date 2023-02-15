
from django.db import models


class MyTableName(models.Model):   
    name = models.CharField(max_length=255)
    class Meta:  
        db_table = "MyTableName"
    def __str__(self):
        return self.name
        
        