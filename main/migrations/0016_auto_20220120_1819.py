# Generated by Django 3.2.8 on 2022-01-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211227_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AlterField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(related_name='teacherClasses', to='main.UserProfile'),
        ),
    ]
