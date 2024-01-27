# Generated by Django 4.2.2 on 2023-02-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer_no', models.CharField(max_length=12, unique=True)),
                ('surname', models.CharField(max_length=20)),
                ('othernames', models.CharField(max_length=30)),
                ('phone_number', models.PositiveIntegerField(unique=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
