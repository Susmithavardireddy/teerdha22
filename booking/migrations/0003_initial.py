# Generated by Django 4.2.3 on 2024-02-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0002_delete_cab_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naviagtion_bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]
