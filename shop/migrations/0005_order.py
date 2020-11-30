# Generated by Django 3.0.5 on 2020-05-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200501_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5111)),
                ('name', models.CharField(max_length=51)),
                ('email', models.CharField(max_length=51)),
                ('phone', models.CharField(max_length=51)),
                ('city', models.CharField(max_length=51)),
                ('state', models.CharField(max_length=51)),
                ('zip_code', models.CharField(max_length=51)),
                ('address', models.CharField(max_length=511)),
            ],
        ),
    ]
