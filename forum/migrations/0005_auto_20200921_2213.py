# Generated by Django 3.0.4 on 2020-09-21 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200921_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='image',
            field=models.ImageField(blank=True, default='cats/cat3.jpg', upload_to=forum.utilities.get_timestamp_path, verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='ForumLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, verbose_name='Like')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('discussion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.Discussion', verbose_name='Дискуссия')),
                ('liked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Поставил лайк')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
    ]
