# Generated by Django 3.1.2 on 2021-01-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210113_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='order_id',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='emp_id',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(default='', null=True, upload_to='uploads/ids/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mob',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='oname',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
