# Generated by Django 3.2.12 on 2022-06-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_image_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocategory',
            options={'ordering': ('name',), 'verbose_name': 'Photo Set Category', 'verbose_name_plural': 'Photo Set Categories'},
        ),
        migrations.AddField(
            model_name='photocategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]