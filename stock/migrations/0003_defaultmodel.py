# Generated by Django 3.1.1 on 2020-09-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200910_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
