# Generated by Django 3.2.6 on 2022-05-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='username',
            field=models.CharField(max_length=30, null=True, verbose_name='username'),
        ),
    ]