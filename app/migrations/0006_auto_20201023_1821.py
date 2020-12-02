# Generated by Django 2.2.2 on 2020-10-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201022_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant_Application_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=8)),
                ('mobile_no', models.IntegerField()),
                ('Adress', models.CharField(max_length=40)),
                ('qualifaction', models.CharField(max_length=10)),
                ('post', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('resume', models.FileField(upload_to='applicant_resume/')),
            ],
        ),
        migrations.AlterField(
            model_name='recurt',
            name='res',
            field=models.CharField(max_length=50),
        ),
    ]
