from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    
    def update_start_date(self):
        self.start_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name
