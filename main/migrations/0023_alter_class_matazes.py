# Generated by Django 3.2.8 on 2022-04-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20220426_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='matazes',
            field=models.ManyToManyField(related_name='matatzClasses', to='main.UserProfile'),
        ),
    ]
