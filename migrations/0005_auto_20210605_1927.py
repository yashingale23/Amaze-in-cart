# Generated by Django 2.2.14 on 2021-06-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('C', 'Computer'), ('M', 'Mobile'), ('OW', 'Accessories')], max_length=2),
        ),
    ]
