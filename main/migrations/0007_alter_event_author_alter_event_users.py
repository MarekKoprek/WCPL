# Generated by Django 5.0.6 on 2024-05-31 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_event_adddate_alter_event_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users_list', to='main.profile'),
        ),
    ]
