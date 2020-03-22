from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    comment = models.TextField()
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
