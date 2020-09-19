# Generated by Django 3.0.4 on 2020-09-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200917_2332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['date_of_creation'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='subanswer',
            options={'ordering': ['date_of_creation'], 'verbose_name': 'Ответ на комментарий', 'verbose_name_plural': 'Ответы на комментарии'},
        ),
        migrations.AlterField(
            model_name='subanswer',
            name='text',
            field=models.TextField(db_index=True, max_length=200, verbose_name=''),
        ),
    ]
