# Generated by Django 2.2 on 2019-04-15 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20190415_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='cost',
        ),
    ]
