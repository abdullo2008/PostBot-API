# Generated by Django 5.1.1 on 2024-09-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_first_name_tgusermodel_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tgusermodel',
            name='tg_id',
            field=models.IntegerField(unique=True),
        ),
    ]
