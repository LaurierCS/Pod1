# Generated by Django 3.2.8 on 2021-12-31 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='url',
            field=models.URLField(max_length=800, unique=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='query',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.query'),
        ),
    ]
