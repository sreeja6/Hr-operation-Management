# Generated by Django 2.2.2 on 2020-10-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_interviewschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantRegisteration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=8)),
                ('mobile_no', models.IntegerField()),
                ('Adress', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
