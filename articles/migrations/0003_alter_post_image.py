# Generated by Django 3.2.5 on 2021-08-30 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210830_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]