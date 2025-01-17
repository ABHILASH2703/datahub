# Generated by Django 5.0.3 on 2024-05-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_educationaldetails_financialdetails_signup_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationaldetails',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='googlepay_id',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='phonepe_id',
        ),
        migrations.AddField(
            model_name='educationaldetails',
            name='cgpa',
            field=models.CharField(default='Default cgpa', max_length=50),
        ),
        migrations.AddField(
            model_name='educationaldetails',
            name='specialization',
            field=models.CharField(default='Default specification', max_length=50),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='election_id',
            field=models.CharField(default='Default election', max_length=50),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='college',
            field=models.CharField(default='Default college', max_length=50),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='degree',
            field=models.CharField(default='Default degree', max_length=50),
        ),
        migrations.AlterField(
            model_name='financialdetails',
            name='pan_number',
            field=models.CharField(default='Default pan', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='address',
            field=models.CharField(default='Default address', max_length=100),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='fullname',
            field=models.CharField(default='Default fullname', max_length=50),
        ),
    ]
