# Generated by Django 3.1.6 on 2021-04-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210401_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('......', '......'), ('Bikes', 'Bikes'), ('Cars', 'Cars'), ('Heavy_Motors', 'Heavy_Motors')], default='', max_length=100),
        ),
    ]
