# Generated by Django 3.2.5 on 2021-07-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='contact',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
