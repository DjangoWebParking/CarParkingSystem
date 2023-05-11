# Generated by Django 3.2.18 on 2023-05-11 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20230511_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingslot',
            name='image',
        ),
        migrations.RemoveField(
            model_name='parkingslot',
            name='reg_date',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=None, upload_to='car_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
