# Generated by Django 3.2.8 on 2022-02-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_result_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='score_neg',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='score_neu',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='score_pos',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='polarity',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
