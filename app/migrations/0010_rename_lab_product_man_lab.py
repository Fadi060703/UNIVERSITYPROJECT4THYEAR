# Generated by Django 5.1.1 on 2024-12-15 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_category_product_categ'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='lab',
            new_name='man_lab',
        ),
    ]
