from django.db import models


class Item(models.Model):
    class Meta:
        db_table = 'items'

    name = models.CharField(verbose_name='商品名', max_length=255)
    price = models.IntegerField(verbose_name='価格')
    comment = models.TextField(verbose_name='コメント')
    img = models.BinaryField(verbose_name='画像')
