# Generated by Django 4.1.1 on 2023-01-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_post_date_alter_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop.tag'),
        ),
    ]