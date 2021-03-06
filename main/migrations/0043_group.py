# Generated by Django 3.2.8 on 2022-05-10 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_class_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ManyToManyField(related_name='groupStudents', to='main.UserProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matatz', to='main.userprofile')),
            ],
        ),
    ]
