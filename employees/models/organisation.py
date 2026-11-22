from django.db import models

class Organisation(models.Model):
    org_id=models.BigAutoField(primary_key=True)
    org_name=models.CharField(max_length=100)
    org_address=models.CharField(max_length=200)

    class Meta:
        db_table='organisation'
