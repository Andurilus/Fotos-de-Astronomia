# Generated by Django 3.2 on 2022-03-31 21:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_auto_20220331_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='apodphoto',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='users.customuser'),
            preserve_default=False,
        ),
    ]
