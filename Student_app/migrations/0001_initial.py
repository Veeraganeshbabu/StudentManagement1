# Generated by Django 4.0.6 on 2022-07-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(max_length=200, null=True)),
                ('StudentName', models.CharField(max_length=50, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('dateOfBirth', models.DateField()),
                ('Graduation', models.CharField(max_length=100, null=True)),
                ('YearOfPass', models.IntegerField(null=True)),
                ('BatchName', models.CharField(max_length=100)),
            ],
        ),
    ]
