# Generated by Django 3.2 on 2022-06-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220602_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_size',
            new_name='has_sizes',
        ),
    ]
