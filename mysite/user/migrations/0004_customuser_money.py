# Generated by Django 4.2.4 on 2023-09-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_telephonecode_code_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='money',
            field=models.PositiveIntegerField(default=0, verbose_name='金币'),
        ),
    ]