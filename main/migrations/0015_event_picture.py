# Generated by Django 5.0.6 on 2024-06-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_event_enddate_alter_event_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(default='blank.jpg', upload_to='event_pics'),
        ),
    ]