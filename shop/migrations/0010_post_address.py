# Generated by Django 3.2 on 2023-01-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]