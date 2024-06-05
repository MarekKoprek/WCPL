# Generated by Django 5.0.4 on 2024-06-04 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_profile_namefirm_profile_website_delete_firm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nameFirm',
            field=models.CharField(default='Nokia', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(default='https://www.nokia.com/', max_length=100, null=True),
        ),
    ]