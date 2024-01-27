# Generated by Django 4.2.2 on 2023-07-17 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_semester_ac_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='ac_year',
        ),
        migrations.AddField(
            model_name='course',
            name='Sem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Students.semester'),
            preserve_default=False,
        ),
    ]
