# Generated by Django 4.1.4 on 2023-01-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
