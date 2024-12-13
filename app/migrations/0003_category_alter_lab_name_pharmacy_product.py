# Generated by Django 5.1.1 on 2024-12-13 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_mainstorgae_product_remove_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lab',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('owner', models.CharField(max_length=50)),
                ('street_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PharmInCity', to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('dose', models.IntegerField()),
                ('needs_perscription', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CatForProd', to='app.category')),
            ],
        ),
    ]