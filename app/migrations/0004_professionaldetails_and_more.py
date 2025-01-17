# Generated by Django 5.0.3 on 2024-05-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_educationaldetails_specification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professionaldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.IntegerField(default=0)),
                ('account', models.IntegerField(default=0)),
                ('pancard', models.CharField(default='pan', max_length=50)),
                ('electionid', models.CharField(default='election', max_length=50)),
                ('drivinglicense', models.CharField(default='license', max_length=50)),
                ('passport', models.CharField(default='passport', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='educationaldetails',
            name='passout_year',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='aadhaar_number',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='election_id',
        ),
        migrations.RemoveField(
            model_name='financialdetails',
            name='pan_number',
        ),
        migrations.RemoveField(
            model_name='personaldetails',
            name='pin',
        ),
        migrations.AddField(
            model_name='educationaldetails',
            name='passoutyear',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='expense_amount1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='expense_amount2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='expense_item1',
            field=models.CharField(default='eitem1', max_length=50),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='expense_item2',
            field=models.CharField(default='eitem2', max_length=50),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='income_amount1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='income_amount2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='income_item1',
            field=models.CharField(default='iitem1', max_length=50),
        ),
        migrations.AddField(
            model_name='financialdetails',
            name='income_item2',
            field=models.CharField(default='iitem2', max_length=50),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='cgpa',
            field=models.CharField(default='cgpa', max_length=50),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='college',
            field=models.CharField(default='college', max_length=50),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='degree',
            field=models.CharField(default='degree', max_length=50),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='specialization',
            field=models.CharField(default='specification', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='fullname',
            field=models.CharField(default='fullname', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='gender',
            field=models.CharField(default='gender', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
