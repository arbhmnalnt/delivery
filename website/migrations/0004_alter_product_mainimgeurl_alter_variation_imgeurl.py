# Generated by Django 4.2.3 on 2023-10-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_product_details_variation_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainImgeUrl',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='رابط الصورة الاساسية'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='imgeUrl',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='رابط الصورة'),
        ),
    ]
