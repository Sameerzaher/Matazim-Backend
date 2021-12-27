# Generated by Django 3.2.8 on 2021-12-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20211227_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='coordinators',
            field=models.ManyToManyField(related_name='coordinatorClasses', to='main.UserProfile'),
        ),
        migrations.AlterField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(related_name='studentClasses', to='main.UserProfile'),
        ),
        migrations.AlterField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(related_name='seacherClasses', to='main.UserProfile'),
        ),
    ]
