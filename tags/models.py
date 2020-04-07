from django.db import models
from django.db.models.signals import pre_save
from product.utils import unique_slug_generator
from product.models import ProductTable


# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(ProductTable, blank=True)

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=ProductTable)
