# Generated by Django 3.2.8 on 2022-04-26 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20220426_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='main.school'),
        ),
        migrations.AlterField(
            model_name='school',
            name='Plan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='main.plan'),
        ),
    ]
