# Generated by Django 3.2.8 on 2022-04-26 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20220426_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='Plan',
        ),
        migrations.RemoveField(
            model_name='class',
            name='school',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]