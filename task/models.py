from django.db import models

# Create your models here.
STATUS =[  
 ( 'P','Pending'),
 ('In', 'In-Progress'),
 ( 'Completed','Completed'),
]

class task(models.Model):
  title= models.CharField(max_length=100)
  description= models.TextField(max_length=255 )
  task_description =models.TextField(max_length=255, null=True)
  status =models.CharField(max_length=10, choices=STATUS, default='pending ')
  due_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  
  
  