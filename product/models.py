from django.db import models


# Create your models here.
class Kinds(models.Model):
    kinds = models.CharField(max_length=60)

    def __str__(self):
        return self.kinds


class Products(models.Model):
    photo = models.ImageField(upload_to='prouct_photo')
    kind = models.ForeignKey(Kinds, on_delete=models.CASCADE)
    body = models.TextField()
    price = models.IntegerField()
    counts = models.IntegerField()

    def __str__(self):
        return str(self.kind)
