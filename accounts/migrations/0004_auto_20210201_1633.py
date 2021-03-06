# Generated by Django 3.1.3 on 2021-02-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210201_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
