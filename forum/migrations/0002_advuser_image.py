# Generated by Django 3.0.4 on 2020-08-24 10:19

from django.db import migrations, models
import forum.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='image',
            field=models.ImageField(blank=True, default='cats/cat3.jpg', upload_to=forum.utilities.get_timestamp_path, verbose_name='Изображение'),
        ),
    ]
