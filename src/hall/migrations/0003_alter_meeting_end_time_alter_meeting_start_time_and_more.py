# Generated by Django 4.0.3 on 2023-06-14 17:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0002_alter_meeting_start_time_alter_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(1, 1, 1, 9, 0)), django.core.validators.MaxValueValidator(datetime.datetime(1, 1, 1, 18, 0))]),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 17, 13, 47, 465253)),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 6, 14, 17, 13, 47, 449631)),
        ),
    ]
