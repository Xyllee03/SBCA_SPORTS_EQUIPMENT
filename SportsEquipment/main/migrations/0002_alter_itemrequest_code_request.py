# Generated by Django 5.1.7 on 2025-03-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='code_request',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
