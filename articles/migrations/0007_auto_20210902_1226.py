# Generated by Django 3.2.5 on 2021-09-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_comment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='articles.IpModel'),
        ),
    ]
