# Generated by Django 5.2.4 on 2025-07-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
