# Generated by Django 5.1.1 on 2024-12-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mainstorageorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
