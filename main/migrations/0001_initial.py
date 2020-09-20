# Generated by Django 3.0.4 on 2020-09-21 00:06

import ckeditor.fields
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('age', models.CharField(max_length=150, verbose_name='Возраст')),
                ('technology_stack', models.TextField(blank=True, verbose_name='Стэк технологий')),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.get_timestamp_path, verbose_name='Изображение')),
                ('info', ckeditor.fields.RichTextField(blank=True, verbose_name='Дополнительная информация')),
            ],
            options={
                'verbose_name': 'Про меня',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название статьи')),
                ('description', models.TextField(db_index=True, max_length=2000, verbose_name='Краткое описание статьи')),
                ('content', ckeditor.fields.RichTextField(blank=True, db_index=True, verbose_name='Текст статьи')),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-date_pub'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text="<span style='font-style:italic;'>Обязательно к заполнению</span>", max_length=150, verbose_name='Ваше имя')),
                ('body', models.TextField(db_index=True, help_text="<span style='font-style:italic;'>Обязательно к заполнению</span>", verbose_name='Текст письма')),
            ],
            options={
                'verbose_name': 'Фидбек',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30, verbose_name='Название проекта')),
                ('description', models.TextField(blank=True, max_length=180, verbose_name='Краткое описание проекта')),
                ('content', ckeditor.fields.RichTextField(blank=True, db_index=True, verbose_name='Описание проекта')),
                ('date_pub', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации проекта')),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.get_timestamp_path, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['-date_pub'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название тэга')),
                ('color', models.CharField(choices=[('RED', 'red'), ('DEFAULT', '#3ba2b9'), ('YELLOW', 'yellow'), ('GREEN', 'green'), ('GRAY', 'gray')], db_index=True, default='#3ba2b9', max_length=30, verbose_name='Цвет тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название поста')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Краткое описание поста')),
                ('content', ckeditor.fields.RichTextField(max_length=2000, verbose_name='Текст поста')),
                ('date_pub', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации поста')),
                ('image', models.ImageField(blank=True, upload_to=main.models.get_timestamp_path, verbose_name='Изображение')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='main.Tag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-date_pub'],
            },
        ),
    ]
