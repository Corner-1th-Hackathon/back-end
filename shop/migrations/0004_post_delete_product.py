# Generated by Django 4.1.1 on 2023-01-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_code', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100)),
                ('name', models.IntegerField(default=0)),
                ('letter', models.TextField()),
                ('image', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
