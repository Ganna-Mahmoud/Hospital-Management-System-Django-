# Generated by Django 4.2 on 2023-06-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_operation_department_alter_doctor_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=10),
        ),
    ]
