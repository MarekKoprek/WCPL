# Generated by Django 5.0.6 on 2024-06-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='event_pics'),
        ),
    ]
