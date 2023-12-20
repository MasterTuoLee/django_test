# Generated by Django 4.2.5 on 2023-09-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelephoneCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('code', models.CharField(max_length=6, verbose_name='验证码')),
            ],
        ),
    ]