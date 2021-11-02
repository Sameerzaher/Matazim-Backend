# Generated by Django 3.2.8 on 2021-10-31 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_usercourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='assignment',
            field=models.CharField(default='aaa', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='main.course'),
        ),
    ]
