# Generated by Django 5.1.7 on 2025-03-27 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBorrow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_no', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipment_name', models.CharField(max_length=255)),
                ('code_request', models.CharField(max_length=20)),
                ('id_student_borrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.studentborrow')),
            ],
        ),
    ]
