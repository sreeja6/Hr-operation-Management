# Generated by Django 2.2.2 on 2020-11-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201028_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalized_candiadates',
            name='f_applicant_id',
            field=models.IntegerField(unique=True),
        ),
    ]
