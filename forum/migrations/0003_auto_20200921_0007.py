# Generated by Django 3.0.4 on 2020-09-21 00:07

from django.db import migrations, models
import forum.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200921_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='image',
            field=models.ImageField(blank=True, default='cats/cat1.jpg', upload_to=forum.utilities.get_timestamp_path, verbose_name='Изображение'),
        ),
    ]
