from django.db import models
from taggit.managers import TaggableManager
from slugify import slugify, SLUG_OK


# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Department(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="القسم")
    
    def __str__(self):
        return self.name

class Product(TimeStampMixin,models.Model):
    nameAr      = models.CharField(max_length=50, null=True, blank=True, verbose_name="الاسم بالعربى")
    nameEn      = models.CharField(max_length=50, null=True, blank=True, verbose_name="الاسم بالانجليزية")
    details     = models.TextField(max_length=500, null=True, blank=True, verbose_name="تفاصيل")
    mainImgeUrl = models.URLField(max_length=250, null=True, blank=True, verbose_name="رابط الصورة الاساسية")
    tags        = TaggableManager()
    slug        = models.SlugField(max_length=250,null=True, blank=True, allow_unicode=True)

    
    
    def formatted_details(self):
        return f'<pre style="white-spaces: pre-wrap;">{self.details}</pre>'
    
    formatted_details.short_description  = "بالتنسيق"

    def __str__(self):
        name = self.nameAr if len(str(self.nameAr))>1 else self.nameEn 
        return name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.nameEn if len(str(self.nameEn))>1 else self.nameAr 
            self.slug = slugify(self.nameAr)
        super().save(*args, **kwargs)

class Variation(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations')
    size        = models.CharField(max_length=50, null=True, blank=True)
    color       = models.CharField(max_length=50, null=True, blank=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    imgeUrl     = models.URLField(max_length=250, null=True, blank=True, verbose_name="رابط الصورة")
    details     = models.TextField(max_length=500, null=True, blank=True, verbose_name="تفاصيل")

    def formatted_details(self):
        return f'<pre style="white-spaces: pre-wrap;">{self.details}</pre>'
    
    formatted_details.short_description  = "بالتنسيق"

    def __str__(self):
        return f"{self.product.nameEn} - {self.size} - {self.color}"