# Generated by Django 5.1.7 on 2025-03-27 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_itemrequest_code_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrequest',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
