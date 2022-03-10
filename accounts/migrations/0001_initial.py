# Generated by Django 3.1.3 on 2022-01-31 04:00

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Porfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile-pic-default.jpg', upload_to=accounts.models.user_profile_image)),
                ('banner', models.ImageField(default='banner-pic-default.jpg', upload_to=accounts.models.user_profile_image)),
                ('bio', models.CharField(help_text='Short Bio (eg. I love cats and games)', max_length=100)),
                ('country', models.CharField(help_text='Enter Your Country', max_length=100)),
                ('city', models.CharField(help_text='Enter Your City', max_length=100)),
                ('twitter_url', models.URLField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('instagram_url', models.URLField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('facebook_url', models.URLField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('github_url', models.URLField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]