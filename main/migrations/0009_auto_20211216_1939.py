# Generated by Django 3.2.8 on 2021-12-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aboutMe',
            field=models.CharField(default='nothing important', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hobbies',
            field=models.CharField(default='games', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='null', max_length=32),
            preserve_default=False,
        ),
    ]