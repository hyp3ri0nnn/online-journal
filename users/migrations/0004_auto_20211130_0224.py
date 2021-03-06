# Generated by Django 3.2.3 on 2021-11-29 23:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20211130_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.TextField(default=datetime.datetime(2021, 11, 29, 23, 24, 0, 515299, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
