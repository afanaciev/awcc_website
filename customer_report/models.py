from django.db import models

# Create your models here.

class Order(models.Model):
    sku = models.CharField(max_length=5)
    slot = models.CharField(max_length=50)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=15)

    def __unicode__(self):
        return self.slot
