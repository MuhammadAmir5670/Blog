# Generated by Django 3.1.3 on 2022-01-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published_on',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post-default.jpg', upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, unique_for_month='published_on'),
        ),
    ]