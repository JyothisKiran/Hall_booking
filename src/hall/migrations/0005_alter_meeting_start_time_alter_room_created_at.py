# Generated by Django 4.0.3 on 2023-06-14 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0004_alter_meeting_end_time_alter_meeting_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 17, 25, 22, 829689)),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 6, 14, 17, 25, 22, 829689)),
        ),
    ]
