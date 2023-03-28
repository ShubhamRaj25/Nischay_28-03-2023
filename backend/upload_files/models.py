from django.db import models


# Create your models here.
class upload_file_details(models.Model):
    # id = models.AutoField(primary_key=True, default=True)
    lead_id = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    date = models.DateTimeField(null=True, default=' ')
    file_name = models.CharField(max_length=50, null=True, default=' ')
    type = models.CharField(max_length=20)

    def __int__(self):
        return (self.lead_id)
