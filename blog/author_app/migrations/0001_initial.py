# Generated by Django 5.1.2 on 2024-11-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('birth_year', models.SmallIntegerField()),
                ('biography', models.TextField()),
            ],
        ),
    ]
