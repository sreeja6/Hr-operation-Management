# Generated by Django 2.2.2 on 2020-10-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_applicantregisteration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantregisteration',
            name='date_of_birth',
            field=models.CharField(max_length=20),
        ),
    ]
